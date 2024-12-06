# import os
# import sys 
# from datetime import datetime
# from PyQt6.QtWidgets import QApplication,QTableWidget,QTableWidgetItem, QWidget,QDateEdit, QComboBox, QLabel,QCheckBox, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
# from PyQt6.QtCore import Qt, QDate
# from PyQt6.QtGui import  QPixmap
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# from view.QSS.SeeSalesQSS import styleSeeSales      
# from controller.ControllerOtherMetods import HistorySalesDay  ,columnHeader
# class SeeSales(QWidget):
#     def resource_path(self, relative_path):
#         """Obtiene la ruta absoluta al recurso, trabajando para dev y para PyInstaller"""
#         try:
#             # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
#             base_path = sys._MEIPASS
#         except Exception:
#             base_path = os.path.abspath(".")
#         return os.path.join(base_path, relative_path)
    
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         # Configuración de la ventana principal
#         self.setWindowTitle('Login')
#         # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
#         self.setFixedHeight(830)
#         self.setFixedWidth(1000)
#         self.generate_form()
#         self.show()

#     def generate_form(self):        
#         central_widget = QWidget()
       
#         # Crear un layout vertical
#         layout = QVBoxLayout(central_widget)
        
#         image_label_see_sales = QLabel()
#         pixmap = QPixmap(self.resource_path('../../Img/ico-historial_de_ventas.png'))  # Ruta relativa de la imagen
#         image_label_see_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         image_label_see_sales.setPixmap(pixmap)
#         image_label_see_sales.setObjectName("image_see_sales") 
        
        
#         label_date=QLabel("Escoja la fecha a ver")
#         label_date.setObjectName("label_date")
#         label_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
#         self.date_Qdate=''
        
#         self.qdate_sales_history = QDateEdit()
#         self.qdate_sales_history.setCalendarPopup(True)
#         self.qdate_sales_history.setObjectName("customDateEdit")
#         self.qdate_sales_history.setDate(QDate.currentDate())

#         # Conectar la señal dateChanged al método date_changed
#         self.qdate_sales_history.dateChanged.connect(self.date_changed)

#         self.data=HistorySalesDay(self.date_Qdate)                                                                     
            
#         # Crear la tabla
#         self.table_widget = QTableWidget()
#         self.table_widget.setRowCount(100)  # Número de filas
#         self.table_widget.setColumnCount(5)  # Número de columnas
#         self.table_widget.setObjectName("customTableWidget") 
#         self.table_widget.setHorizontalHeaderLabels(columnHeader())
#         # Llenar la tabla con datos de ejemplo
#         for cont_row in range(0,len(self.data),1 ):
#                 nombre_item=QTableWidgetItem(self.data[cont_row][0])
#                 self.table_widget.setItem(cont_row,0, nombre_item)
#                 cantidad_item=QTableWidgetItem(self.data[cont_row][0])
#                 self.table_widget.setItem(cont_row,0, cantidad_item)
#                 precio_unidad_item=QTableWidgetItem(self.data[cont_row][0])
#                 self.table_widget.setItem(cont_row,0, precio_unidad_item)
#                 fecha_item=QTableWidgetItem(self.data[cont_row][0])
#                 self.table_widget.setItem(cont_row,0, fecha_item)
#                 subtotal_item=QTableWidgetItem(self.data[cont_row][0])
#                 self.table_widget.setItem(cont_row,0, subtotal_item)
        
#         # Crear una área de desplazamiento
#         scroll_area = QScrollArea()
#         scroll_area.setWidget(self.table_widget)
#         scroll_area.setWidgetResizable(True)

#         message_total="TOTAL:0"
#         label_total=QLabel(message_total)
#         label_total.setObjectName("label_total")
#         label_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
#         layout.addWidget(image_label_see_sales)        
#         layout.addWidget(label_date)
#         layout.addWidget(self.qdate_sales_history)
#         layout.addWidget(scroll_area)
#         layout.addWidget(label_total)

#         self.setLayout(layout)

#     def formaterDate(date_register):
#         return date_register.strftime("%Y-%m-%d")
#     def date_changed(self):
#         # Obtener la fecha seleccionada como cadena
#         selected_date = self.qdate_sales_history.date().toString("dd-MM-yyyy")

#         # Guardar la fecha seleccionada en self.date_Qdate
#         self.date_Qdate = selected_date
# # Ejecutar la aplicación
# app = QApplication(sys.argv)
# app.setStyleSheet(styleSeeSales())
# window = SeeSales()
# sys.exit(app.exec())
import os
import sys
from PyQt6.QtWidgets import QApplication,QSizePolicy, QTableWidget,QHeaderView, QTableWidgetItem, QWidget, QDateEdit, QLabel, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QPixmap
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.SeeSalesQSS import styleSeeSales      
from controller.ControllerOtherMetods import HistorySalesDay, columnHeaderTableSeeSales

class SeeSales(QWidget):
    def resource_path(self, relative_path):
        """Obtiene la ruta absoluta al recurso, trabajando para dev y para PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Historial de Ventas')
        self.setFixedHeight(830)
        self.setFixedWidth(1000)
        self.generate_form()
        self.show()

    def generate_form(self):        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        image_label_see_sales = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico-historial_de_ventas.png'))  # Ruta relativa de la imagen
        image_label_see_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_see_sales.setPixmap(pixmap)
        image_label_see_sales.setObjectName("image_see_sales") 
        
        label_date = QLabel("Escoja la fecha a ver")
        label_date.setObjectName("label_date")
        label_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.date_Qdate = ''
        
        self.qdate_sales_history = QDateEdit()
        self.qdate_sales_history.setCalendarPopup(True)
        self.qdate_sales_history.setObjectName("customDateEdit")
        self.qdate_sales_history.setDate(QDate.currentDate())

        # Conectar la señal dateChanged al método date_changed
        self.qdate_sales_history.dateChanged.connect(self.date_changed)

        self.data = HistorySalesDay(self.date_Qdate)
        
        # Crear la tabla
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(100)  # Número de filas
        self.table_widget.setColumnCount(5)  # Número de columnas
        self.table_widget.setObjectName("customTableWidget") 
        self.table_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_widget.setHorizontalHeaderLabels(columnHeaderTableSeeSales())
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.fill_table(self.data)
        
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table_widget)
        scroll_area.setWidgetResizable(True)

        self.label_total = QLabel("TOTAL:0")
        self.label_total.setObjectName("label_total")
        self.label_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
        layout.addWidget(image_label_see_sales)        
        layout.addWidget(label_date)
        layout.addWidget(self.qdate_sales_history)
        layout.addWidget(scroll_area)
        layout.addWidget(self.label_total)

        self.setLayout(layout)

    def fill_table(self, data):
        # Limpiar la tabla antes de llenarla con nuevos datos
        self.table_widget.clearContents()
        
        for cont_row, row_data in enumerate(data):
            for cont_col, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                self.table_widget.setItem(cont_row, cont_col, item)
        


    def date_changed(self):
        selected_date = self.qdate_sales_history.date().toString("dd-MM-yyyy")
        self.date_Qdate = selected_date
        self.data = HistorySalesDay(self.date_Qdate)
        self.fill_table(self.data)

# Ejecutar la aplicación
app = QApplication(sys.argv)
app.setStyleSheet(styleSeeSales())
window = SeeSales()
sys.exit(app.exec())
