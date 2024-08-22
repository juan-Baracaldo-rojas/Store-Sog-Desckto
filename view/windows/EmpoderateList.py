import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QDateEdit, QLabel,QCheckBox, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import  QPixmap
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from controller.ControllerOtherMetods import empowermentList
from view.QSS.EmpoderateListQSS import styleEmpoderateList

class EmpoderateList(QWidget):
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
        self.setFixedWidth(730)
        self.generate_form()
        self.show()

    def generate_form(self):
        
        self.checkboxes = []
        options = empowermentList()
        central_widget=QWidget()
        layout=QGridLayout(central_widget)
        
        label_title_empoderate_list=QLabel("LISTA DE TAREAS RECOMENDADAS")
        label_title_empoderate_list.setObjectName("title_empoderate_list")
        label_title_empoderate_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_label_empoderate_list = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_lista_empoderamiento.png'))  # Ruta relativa de la imagen
        image_label_empoderate_list.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_empoderate_list.setPixmap(pixmap)
        image_label_empoderate_list.setObjectName("image_empoderate_list") 
        
        layout.addWidget(label_title_empoderate_list,0,0,1,3)
        layout.addWidget(image_label_empoderate_list,1,0,1,3)

        
        for cont in range(0,len(options),1):
            checkbox = QCheckBox(options[cont])
            checkbox.stateChanged.connect(self.check_limit)
            self.checkboxes.append(checkbox)
            # conditionLenghtMin=cont < (len(options)/2)
            # if conditionLenghtMin:
            # layout.addWidget(checkbox,cont+4,1)
            layout.addWidget(checkbox,cont+2,1)
            # elif not conditionLenghtMin:
                # layout.addWidget(checkbox,cont+1,2)

        self.setLayout(layout)

    def check_limit(self):
        # Contar cuántos checkboxes están seleccionados
        checked_count = sum(1 for checkbox in self.checkboxes if checkbox.isChecked())

        # Deshabilitar checkboxes adicionales si ya hay 3 seleccionados
        if checked_count >= 3:
            for checkbox in self.checkboxes:
                if not checkbox.isChecked():
                    checkbox.setEnabled(False)
        else:
            for checkbox in self.checkboxes:
                checkbox.setEnabled(True)

     
app = QApplication(sys.argv)

app.setStyleSheet(styleEmpoderateList())

window = EmpoderateList()
sys.exit(app.exec())
       
    
    