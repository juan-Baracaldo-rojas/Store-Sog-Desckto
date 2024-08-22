import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QLabel, QPushButton,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.ReportMenuQSS import styleReportMenu

class ReportMenu(QWidget):
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
        self.setWindowTitle('Menu Reporte')
        # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
        self.setFixedHeight(630)
        self.setFixedWidth(530)
        self.generate_form()
        self.show()
    
    def generate_form(self):
        image_label_report = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_menu_reportes.png'))  # Ruta relativa de la imagen
        image_label_report.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_report.setPixmap(pixmap)
        image_label_report.setObjectName("image_reporte") 

        btn_daily_sales=QPushButton("Ventas por dia")
        btn_daily_sales.setObjectName("btn_daily_sales")
        
        btn_month_sales=QPushButton("Ventas por mes")
        btn_month_sales.setObjectName("btn_month_sales")
        
        btn_year_sales=QPushButton("Ventas por año")
        btn_year_sales.setObjectName("btn_year_sales")


        principalWidget=QWidget()
        layout=QGridLayout(principalWidget)
        layout.addWidget(image_label_report)
        layout.addWidget(btn_daily_sales)
        layout.addWidget(btn_month_sales)
        layout.addWidget(btn_year_sales)

        self.setLayout(layout)

app = QApplication(sys.argv)

app.setStyleSheet(styleReportMenu())

window = ReportMenu()
sys.exit(app.exec())
