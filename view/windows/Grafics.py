import sys
from datetime import date
import os
import seaborn as sns
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QVBoxLayout,QWidget, QDateEdit,QComboBox, QLabel, QSizePolicy, QPushButton,QHBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.GraficsQSS import styleGrafics
from controller.ControllerOtherMetods import dataGraficLineHistorySalesYear,dataGraficLineHistorySalesMonth,colorGenerator,optionsComboBoxGrafics,list_best_products,dataGraficLineHistorySalesDaily,numberMonth,all_products_invetory_Expire

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        # Crear la figura y los ejes
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)

class Grafics(QWidget):

    def resource_path(self, relative_path):
        """Obtiene la ruta absoluta al recurso, trabajando para dev y para PyInstaller"""
        try:
            # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def __init__(self,typeReport):
        super().__init__()
        self._typeReport=typeReport
        self.dataDay=[]
        self.dataMonth=[]
        self.dataYear=[]
        self.date_actualy=date.today()
        self.label_cant_sell_infomation=QLabel("")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.init_ui()

    def init_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Histograma de Nombres y Resultados')
        self.setFixedHeight(820)
        self.setFixedWidth(1450)
        self.generate_form()
        # self.show()

    def GraficTop10(self):
        # Datos para el histograma
        datos=list_best_products()
        names = [item[0] for item in datos]
        ganancies = [item[1] for item in datos]
        # Crear el widget de canvas para la gráfica
        canvas = MplCanvas(self, width=5, height=3, dpi=100)
         # Configurar el QSizePolicy para que el widget se expanda
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Crear el gráfico de barras
        sns.barplot(x=names, y=ganancies, hue=names, ax=canvas.ax, palette="Greens_d")

        # Añadir la leyenda a los ejes
        canvas.ax.set_xlabel("Nombres")
        canvas.ax.set_ylabel("Valores")
        canvas.ax.set_title("Histograma productos top 10")

        return canvas
    
    def graficSalesDay(self,date_sale):
      # Crear el canvas de la gráfica
        canvas = MplCanvas(self, width=5, height=3, dpi=100)

         # Configurar el QSizePolicy para que el widget se expanda
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # Datos para el gráfico de líneas
        palete_color_rgb=colorGenerator(1)
        self.dataDay=dataGraficLineHistorySalesDaily(date_sale)
        self.updateLabelCantSales(self.dataDay)
        day=[item[0] for item in self.dataDay ]
        sales=[item[1] for item in self.dataDay]

        # Crear el gráfico de líneas
        sns.barplot(x=day, y=sales, hue=day, ax=canvas.ax)
        canvas.ax.set_xlabel(f"Fecha {date_sale}")
        canvas.ax.set_ylabel("Total venta")
        canvas.ax.set_title(f"Histograma ventas totales {date_sale}")
        return canvas
    

    def graficSalesMonth(self,month,year):
      # Crear el canvas de la gráfica
        canvas = MplCanvas(self, width=5, height=3, dpi=100)

         # Configurar el QSizePolicy para que el widget se expanda
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Datos para el gráfico de líneas
        palete_color_rgb=colorGenerator(1)
        self.dataMonth=dataGraficLineHistorySalesMonth(month,year)
        self.updateLabelCantSales(self.dataMonth)
        days=[item[0] for item in self.dataMonth ]
        sales=[item[1] for item in self.dataMonth]

        # Crear el gráfico de líneas
        sns.lineplot(x=days, y=sales, marker='o', color='b', linestyle='-', linewidth=2, ax=canvas.ax)
        canvas.ax.set_xlabel(f"dias de {month} del {year}")
        canvas.ax.set_ylabel("Total venta")
        canvas.ax.set_title(f"ventas totales del mes {month} del año {year}")
        return canvas
    
    def graficSalesYear(self,year):
      # Crear el canvas de la gráfica
        canvas = MplCanvas(self, width=5, height=3, dpi=100)

         # Configurar el QSizePolicy para que el widget se expanda
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Datos para el gráfico de líneas
        palete_color_rgb=colorGenerator(1)
        self.dataYear=dataGraficLineHistorySalesYear(year)
        self.updateLabelCantSales(self.dataYear)
        days=[item[0] for item in self.dataYear ]
        sales=[item[1] for item in self.dataYear]

        # Crear el gráfico de líneas
        sns.lineplot(x=days, y=sales, marker='o', color='b', linestyle='-', linewidth=2, ax=canvas.ax)
        canvas.ax.set_xlabel(f"meses del {year}")
        canvas.ax.set_ylabel("Total venta")
        canvas.ax.set_title(f"ventas totales del año {year} por mes")
        return canvas
    
    def updateGraficDay(self):
        # self.sales_day=self.graficSalesDay(self.date_day.date().toString("yyyy-MM-dd"))
        if hasattr(self, 'sales_day') and self.sales_day is not None:
            self.sales_day.setParent(None)  # Elimina el widget de la gráfica anterior

             # Actualizar la gráfica con la nueva fecha seleccionada
        selected_date = self.date_day.date().toString("dd-MM-yyyy")
        self.sales_day = self.graficSalesDay(str(selected_date))
        
        # Agregar la nueva gráfica al layout
        self.layout_principal.addWidget(self.sales_day, 2, 1)
    
    def updateGraficMonth(self):
        # self.sales_day=self.graficSalesDay(self.date_day.date().toString("yyyy-MM-dd"))
        if hasattr(self, 'month_sales') and self.month_sales is not None:
            self.month_sales.setParent(None)  # Elimina el widget de la gráfica anterior

             # Actualizar la gráfica con la nueva fecha seleccionada
        numMonth=numberMonth(self.unidComboBox.currentText())
        self.month_sales = self.graficSalesMonth(str(numMonth),str(self.spiner_year.value()))
        
        # Agregar la nueva gráfica al layout
        self.layout_principal.addWidget(self.month_sales, 2, 1)
        
    def contar_tuplas_validas(self,tuplas):
        sum=0
        for cont in range(0,len(tuplas),1):
            if tuplas[cont][0]!=None and tuplas[cont][1]!=None:
                sum=sum+1
        return sum    

    def updateYear(self):
         # self.sales_day=self.graficSalesDay(self.date_day.date().toString("yyyy-MM-dd"))
        if hasattr(self, 'year_sales') and self.year_sales is not None:
            self.year_sales.setParent(None)  # Elimina el widget de la gráfica anterior

             # Actualizar la gráfica con la nueva fecha seleccionada
        
        self.year_sales = self.graficSalesYear(str(self.spiner_year.value()))
        
        # Agregar la nueva gráfica al layout
        self.layout_principal.addWidget(self.year_sales, 2, 1)

    def updateLabelCantSales(self,data):
        condition_day=self._typeReport=='day'
        condition_month=self._typeReport=='month'
        condition_year=self._typeReport=='year'
        if condition_day:
            self.label_cant_sell_infomation.setText(f"CANTIDAD PRODUCTOS \nVENDIDO {str(self.contar_tuplas_validas(data))}")
        if condition_month:
            self.label_cant_sell_infomation.setText(f"CANTIDAD PRODUCTOS \nVENDIDO {str(self.contar_tuplas_validas(data))}")
        if condition_year:
            self.label_cant_sell_infomation.setText(f"CANTIDAD PRODUCTOS \nVENDIDO {str(self.contar_tuplas_validas(data))}")
        
        
    def generate_form(self):
        
        condition_day=self._typeReport=='day'
        condition_month=self._typeReport=='month'
        condition_year=self._typeReport=='year'
        principalWidget = QWidget()
        self.layout_principal = QGridLayout(principalWidget)

        widgetMenu = QWidget()
        layout_options = QGridLayout(widgetMenu)

        # Imagen
        image_label_grafics = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_reporte.png'))
        image_label_grafics.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_grafics.setPixmap(pixmap)
        image_label_grafics.setObjectName("image_Descargas")

        # Labels y Combos
        label_month = QLabel("Escoja el mes")
        label_month.setObjectName("label_month")
        label_month.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.unidComboBox = QComboBox()
        options = optionsComboBoxGrafics()
        self.unidComboBox.addItems(options)
        self.unidComboBox.currentTextChanged.connect(self.updateGraficMonth)
        
        
        
        label_day = QLabel("Escoja el Dia")
        label_day.setObjectName("label_day")
        label_day.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.date_day = QDateEdit(QDate.currentDate())
        self.date_day.setObjectName("date_day")
        self.date_day.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_day.dateChanged.connect(self.updateGraficDay)

        label_year = QLabel("Escriba el año")
        label_year.setObjectName("label_year")
        label_year.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spiner_year = QSpinBox()
        self.spiner_year.setObjectName("spiner_year")
        self.spiner_year.setMaximum(3000)
        self.spiner_year.setMinimum(2022)
        self.spiner_year.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if condition_month:
            self.spiner_year.valueChanged.connect(self.updateGraficMonth)
        if condition_year:
            self.spiner_year.valueChanged.connect(self.updateYear)
        # Agregar widgets al self.layout_principal de opciones
        if condition_day:
            layout_options.addWidget(label_day,0,0)
            layout_options.addWidget(self.date_day,1,0)
        if condition_month:    
            layout_options.addWidget(label_month,0,0)
            layout_options.addWidget(self.unidComboBox,1,0)
            layout_options.addWidget(label_year,0,1)
            layout_options.addWidget(self.spiner_year,1,1)
        if condition_year:    
            layout_options.addWidget(label_year,0,0)
            layout_options.addWidget(self.spiner_year,1,0)

        top_10=self.GraficTop10()
        self.sales_day=""
        self.month_sales=""
        self.year_sales=""
        if condition_day :   
            self.sales_day=self.graficSalesDay(str(self.date_actualy))
        if condition_month:
            self.month_sales=self.graficSalesMonth(str(self.date_actualy.month),str(self.date_actualy.year))
        if condition_year:
            self.year_sales=self.graficSalesYear(str(self.date_actualy.year))
          # Crear un QScrollArea y colocar el widget dentro de ella
       
        widget_label_information=QWidget()
        widget_label_information.setObjectName("info")
        layout_information=QHBoxLayout(widget_label_information)

        num_sales=0
        self.label_cant_sell_infomation = QLabel(f"CANTIDAD PRODUCTOS \nVENDIDO {num_sales}")
        self.label_cant_sell_infomation.setObjectName("label_cant")
        self.label_cant_sell_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        num_sales=len(all_products_invetory_Expire())
        label_cant_EXPIRATION_infomation = QLabel(f"CANTIDAD PRODUCTOS \nVENCIDOS {num_sales}")
        label_cant_EXPIRATION_infomation.setObjectName("label_cant")
        label_cant_EXPIRATION_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        num_sales=2
        label_cant_product_stock_infomation = QLabel(f"CANTIDAD PRODUCTOS  \nEN STOCK:{num_sales}")
        label_cant_product_stock_infomation.setObjectName("label_cant")
        label_cant_product_stock_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_information.addWidget(self.label_cant_sell_infomation)
        layout_information.addWidget(label_cant_EXPIRATION_infomation)
        layout_information.addWidget(label_cant_product_stock_infomation)

        #TODO falta vincular el numero de ventas segun el numero de ventas que halla

        # Agregar widgets al self.layout_principal principal
        if condition_day:
            self.layout_principal.addWidget(image_label_grafics, 0, 0, 1, 2)
            self.layout_principal.addWidget(widgetMenu, 1, 0,1,2)
            self.layout_principal.addWidget(top_10, 2, 0)
            self.layout_principal.addWidget(self.sales_day, 2, 1)
        if condition_month:
            self.layout_principal.addWidget(image_label_grafics, 0, 0, 1, 2)
            self.layout_principal.addWidget(widgetMenu, 1, 0,1,2)
            self.layout_principal.addWidget(top_10, 2, 0)
            self.layout_principal.addWidget(self.month_sales,2,1)
        if condition_year:
            self.layout_principal.addWidget(image_label_grafics, 0, 0, 1, 2)
            self.layout_principal.addWidget(widgetMenu, 1, 0,1,2)
            self.layout_principal.addWidget(top_10, 2, 0)
            self.layout_principal.addWidget(self.year_sales,2,1)
        self.layout_principal.addWidget(widget_label_information,3,0,1,2)
        
        self.setLayout(self.layout_principal)
        
   
def main():
    app = QApplication(sys.argv)
    ventana = Grafics()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()