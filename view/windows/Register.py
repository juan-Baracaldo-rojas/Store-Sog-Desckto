import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QLabel, QPushButton,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.RegisterQSS import qssStyleCategory
from controller.ControllerOtherMetods import update_user
from model.User import Local

class Register(QWidget):
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
                
        image_label = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_login.png'))  # Ruta relativa de la imagen
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setPixmap(pixmap)
        image_label.setObjectName("image") 
        
        label_name_local=QLabel("Digite el nombre del local")
        label_name_local.setObjectName("name_local")
        label_name_local.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_name_local=QLineEdit()
        self.input_name_local.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label_type_local=QLabel("Escoga las 3 principales funciones de su local")
        label_type_local.setObjectName("type_local")
        label_type_local.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.checkboxes = []
        options = self.options()
        central_widget = QWidget()
        central_widget.setObjectName("container")
        layout=QGridLayout(central_widget)
        # layout.addWidget(title_register,0,0,1,2)
        layout.addWidget(image_label,0,0,1,4)
        layout.addWidget(label_name_local,1,0,1,4)
        layout.addWidget(self.input_name_local,2,0,1,4)
        layout.addWidget(label_type_local,3,0,1,4)

        layout.setObjectName("container-register")

        for cont in range(0,len(options),1):
            checkbox = QCheckBox(options[cont])
            checkbox.stateChanged.connect(self.check_limit)
            self.checkboxes.append(checkbox)
            conditionLenghtMin=cont < (len(options)/2)
            if conditionLenghtMin:
                layout.addWidget(checkbox,cont+4,1)
            elif not conditionLenghtMin:
                layout.addWidget(checkbox,cont+1,2)

        # Establecer el layout

        btnSave=QPushButton('Guardar')
        btnSave.setObjectName("btn_Save")
        btnSave.clicked.connect(self.modifyLocal)
        layout.addWidget(btnSave,10,0,1,4)
        self.setLayout(layout)

    def get_selected_options(self):
        selected_options = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                selected_options.append(checkbox.text())  # Agregar el texto del checkbox seleccionado a la lista
        return selected_options

    def modifyLocal(self):
        options=self.get_selected_options()
        condition_lenght_minimun_1=len(options) ==1
        condition_lenght_minimun_2=len(options) ==2
        condition_lenght_minimun_3=len(options) ==3
        local=""
        if condition_lenght_minimun_1:
            local=Local(self.input_name_local.text(),options[0],"Jugueteria","Papeleria")
        if condition_lenght_minimun_2:
            local=Local(self.input_name_local.text(),options[0],options[1],"Papeleria")
        if condition_lenght_minimun_3:
            local=Local(self.input_name_local.text(),options[0],options[1],options[2])
        update_user(local)

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
        
    
    def options(self):
        return ['Papeleria', 'Jugueteria', 'Servicio de Impresiones', 'Ropa', 'Venta de Comestibles','Zapateria']

app = QApplication(sys.argv)
app.setStyleSheet(qssStyleCategory())

window = Register()
sys.exit(app.exec())
