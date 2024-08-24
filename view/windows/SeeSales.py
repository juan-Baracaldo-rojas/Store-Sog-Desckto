import os
import sys 
from datetime import datetime
from PyQt6.QtWidgets import QApplication,QTableWidget,QTableWidgetItem, QWidget,QDateEdit, QComboBox, QLabel,QCheckBox, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import  QPixmap
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.SeeSalesQSS import styleSeeSales        
class SeeSales(QWidget):
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
        self.init_ui()

    def init_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Login')
        # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
        self.setFixedHeight(830)
        self.setFixedWidth(1000)
        self.generate_form()
        self.show()

    def generate_form(self):        
        central_widget = QWidget()
       
        # Crear un layout vertical
        layout = QVBoxLayout(central_widget)
        
        image_label_see_sales = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico-historial_de_ventas.png'))  # Ruta relativa de la imagen
        image_label_see_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_see_sales.setPixmap(pixmap)
        image_label_see_sales.setObjectName("image_see_sales") 
        
        
        label_date=QLabel("Escoja la fecha a ver")
        label_date.setObjectName("label_date")
        label_date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        qdate_sales_history = QDateEdit()
        qdate_sales_history.setCalendarPopup(True)
        qdate_sales_history.setObjectName("customDateEdit")
        qdate_sales_history.setDate(QDate.currentDate())
            
        # Crear la tabla
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(100)  # Número de filas
        self.table_widget.setColumnCount(10)  # Número de columnas
        self.table_widget.setObjectName("customTableWidget") 
        
        # Llenar la tabla con datos de ejemplo
        for row in range(100):
            for column in range(10):
                item = QTableWidgetItem(f"Item {row},{column}")
                self.table_widget.setItem(row, column, item)
        
        # Crear una área de desplazamiento
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table_widget)
        scroll_area.setWidgetResizable(True)

        message_total="TOTAL:0"
        label_total=QLabel(message_total)
        label_total.setObjectName("label_total")
        label_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
        layout.addWidget(image_label_see_sales)        
        layout.addWidget(label_date)
        layout.addWidget(qdate_sales_history)
        layout.addWidget(scroll_area)
        layout.addWidget(label_total)

        self.setLayout(layout)

    def formaterDate(date_register):
        return date_register.strftime("%Y-%m-%d")
# Ejecutar la aplicación
app = QApplication(sys.argv)
app.setStyleSheet(styleSeeSales())
window = SeeSales()
sys.exit(app.exec())