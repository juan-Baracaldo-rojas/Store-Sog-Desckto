import sys
import os
import seaborn as sns
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QVBoxLayout,QWidget, QDateEdit,QComboBox, QLabel, QSizePolicy, QPushButton,QHBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.GraficsQSS import styleGrafics
from controller.ControllerOtherMetods import dataGraficLineHistorySalesYear,dataGraficLineHistorySalesMonth,colorGenerator,optionsComboBoxGrafics,list_best_products,dataGraficLineHistorySalesDaily

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
    
    def __init__(self):
        super().__init__()
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
        datos=dataGraficLineHistorySalesDaily('10-12-2022')
        day=[item[0] for item in datos ]
        sales=[item[1] for item in datos]

        # Crear el gráfico de líneas
        sns.barplot(x=day, y=sales, hue=day, ax=canvas.ax)
        canvas.ax.set_xlabel("Fecha")
        canvas.ax.set_ylabel("Total venta")
        canvas.ax.set_title(f"Histograma ventas totales")
        return canvas
    

    def graficSalesMonth(self,month,year):
      # Crear el canvas de la gráfica
        canvas = MplCanvas(self, width=5, height=3, dpi=100)

         # Configurar el QSizePolicy para que el widget se expanda
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Datos para el gráfico de líneas
        palete_color_rgb=colorGenerator(1)
        datos=dataGraficLineHistorySalesMonth(month,year)
        days=[item[0] for item in datos ]
        sales=[item[1] for item in datos]

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
        datos=dataGraficLineHistorySalesYear(year)
        days=[item[0] for item in datos ]
        sales=[item[1] for item in datos]

        # Crear el gráfico de líneas
        sns.lineplot(x=days, y=sales, marker='o', color='b', linestyle='-', linewidth=2, ax=canvas.ax)
        canvas.ax.set_xlabel(f"meses del {year}")
        canvas.ax.set_ylabel("Total venta")
        canvas.ax.set_title(f"ventas totales del año {year} por mes")
        return canvas
    

    def generate_form(self):
        principalWidget = QWidget()
        layout_principal = QGridLayout(principalWidget)

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

        unidComboBox = QComboBox()
        options = optionsComboBoxGrafics()
        unidComboBox.addItems(options)

        label_day = QLabel("Escoja el Dia")
        label_day.setObjectName("label_day")
        label_day.setAlignment(Qt.AlignmentFlag.AlignCenter)

        date_day = QDateEdit(QDate.currentDate())
        date_day.setObjectName("date_day")
        date_day.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_year = QLabel("Escriba el año")
        label_year.setObjectName("label_year")
        label_year.setAlignment(Qt.AlignmentFlag.AlignCenter)

        spiner_year = QSpinBox()
        spiner_year.setObjectName("spiner_year")
        spiner_year.setMaximum(3000)
        spiner_year.setMinimum(2023)
        spiner_year.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Agregar widgets al layout_principal de opciones
        layout_options.addWidget(label_month,0,0)
        layout_options.addWidget(unidComboBox,1,0)
        layout_options.addWidget(label_day,0,1)
        layout_options.addWidget(date_day,1,1)
        layout_options.addWidget(label_year,0,2)
        layout_options.addWidget(spiner_year,1,2)

        top_10=self.GraficTop10()
        sales_day=self.graficSalesDay('10-12-2022')
        month_sales=self.graficSalesMonth('12','2022')
        year_sales=self.graficSalesYear('2022')
          # Crear un QScrollArea y colocar el widget dentro de ella
       
        widget_label_information=QWidget()
        widget_label_information.setObjectName("info")
        layout_information=QHBoxLayout(widget_label_information)

        num_sales=2
        label_cant_sell_infomation = QLabel(f"CANTIDAD PRODUCTOS \nVENDIDO {num_sales}")
        label_cant_sell_infomation.setObjectName("label_cant")
        label_cant_sell_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        num_sales=2
        label_cant_EXPIRATION_infomation = QLabel(f"CANTIDAD PRODUCTOS \nVENCIDOS {num_sales}")
        label_cant_EXPIRATION_infomation.setObjectName("label_cant")
        label_cant_EXPIRATION_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        num_sales=2
        label_cant_product_stock_infomation = QLabel(f"CANTIDAD PRODUCTOS  \nEN STOCK:{num_sales}")
        label_cant_product_stock_infomation.setObjectName("label_cant")
        label_cant_product_stock_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_information.addWidget(label_cant_sell_infomation)
        layout_information.addWidget(label_cant_EXPIRATION_infomation)
        layout_information.addWidget(label_cant_product_stock_infomation)

        # Agregar widgets al layout_principal principal
        layout_principal.addWidget(image_label_grafics, 0, 0, 1, 2)
        layout_principal.addWidget(widgetMenu, 1, 0,1,2)
        layout_principal.addWidget(top_10, 2, 0)
        layout_principal.addWidget(sales_day, 2, 1)
        layout_principal.addWidget(month_sales,3,0)
        layout_principal.addWidget(year_sales,3,1)
        layout_principal.addWidget(widget_label_information,4,0,1,2)
        
        self.setLayout(layout_principal)
        
   
def main():
    app = QApplication(sys.argv)
    ventana = Grafics()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()