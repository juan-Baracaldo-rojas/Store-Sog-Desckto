import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QDateEdit, QLabel, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.DowloadsQSS import styleDowloads

class Dowloads(QWidget):
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
        self.setFixedHeight(630)
        self.setFixedWidth(530)
        self.generate_form()
        self.show()

    def generate_form(self):
        
        image_label_dowloads = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_descargas.png'))  # Ruta relativa de la imagen
        image_label_dowloads.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_dowloads.setPixmap(pixmap)
        image_label_dowloads.setObjectName("image_Descargas") 

        label_date_dowload_sales=QLabel("Escoja el dia que desea descargar")
        label_date_dowload_sales.setObjectName("date_dowload_sales")
        label_date_dowload_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        qdate_dowload_sales = QDateEdit()
        qdate_dowload_sales.setCalendarPopup(True)
        qdate_dowload_sales.setDate(QDate.currentDate())

        btn_dowloads_products=QPushButton("Descargar productos")
        btn_dowloads_products.setObjectName("btn_dowloads_products")
        
        btn_dowloads_category=QPushButton("Descargar Categoria")
        btn_dowloads_category.setObjectName("btn_dowloads_category")
        
        btn_download_day_sales=QPushButton("Descargar Ventas del dia")
        btn_download_day_sales.setObjectName("btn_download_day_sales")


        principalWidget=QWidget()
        layout=QVBoxLayout(principalWidget)
        layout.addWidget(image_label_dowloads)
        layout.addWidget(label_date_dowload_sales)
        layout.addWidget(qdate_dowload_sales)
        layout.addWidget(btn_dowloads_products)
        layout.addWidget(btn_dowloads_category)
        layout.addWidget(btn_download_day_sales)

        self.setLayout(layout)

app = QApplication(sys.argv)
app.setStyleSheet(styleDowloads())
window = Dowloads()
sys.exit(app.exec())
