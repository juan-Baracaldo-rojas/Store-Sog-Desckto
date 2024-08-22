import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem,QComboBox, QLabel, QPushButton,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea,QDateEdit
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.ProductQSS import styleProduct

class Product(QWidget):
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
        self.setWindowTitle('Formulario de Producto')
        # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
        self.setFixedHeight(730)
        self.setFixedWidth(1200)
        self.generate_form()
        self.show()

    def generate_form(self):
                   
        image_label = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_productos.png'))  # Ruta relativa de la imagen
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setPixmap(pixmap)
        image_label.setObjectName("image") 

        label_name_product=QLabel("Digite el nombre del producto")
        label_name_product.setObjectName("name_product")
        # label_name_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        input_name_product=QLineEdit()
        input_name_product.setObjectName("input_name_product")
        # input_name_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label_marc_product=QLabel("Digite la marca del producto")
        label_marc_product.setObjectName("marc_product")
        # label_marc_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        input_marc_product=QLineEdit()
        input_marc_product.setObjectName("input_marc_product")
        # input_marc_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_price_product=QLabel("Digite el precio del producto")
        label_price_product.setObjectName("price_product")
        # label_price_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        spiner_price_product=QSpinBox()
        spiner_price_product.setObjectName("spiner_price_product")
        spiner_price_product.setMaximum(9999999)
        spiner_price_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
       
        label_unid_product=QLabel("Escoja la unidad del producto")
        label_unid_product.setObjectName("unid_product")
        # label_unid_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        unidComboBox = QComboBox()
        options=self.optionsComboBox()
        unidComboBox.addItems(options)
       
        label_size_product=QLabel("Digite la talla o tamaño del producto del producto")
        label_size_product.setObjectName("size_product")
        # label_size_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        input_size_product=QLineEdit()
        input_size_product.setObjectName("input_size_product")
        input_size_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_color_product=QLabel("Digite el color del producto del producto")
        label_color_product.setObjectName("color_product")
        # label_color_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        input_color_product=QLineEdit()
        input_color_product.setObjectName("input_color_product")
        # input_color_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_date_expire_product=QLabel("Escoja la fecha de vencimiento del producto")
        label_date_expire_product.setObjectName("date_expire_product")
        
        qdate_expire_date_product = QDateEdit()
        qdate_expire_date_product.setCalendarPopup(True)
        qdate_expire_date_product.setDate(QDate.currentDate())


        label_material_product=QLabel("Escriba el material del producto del producto")
        label_material_product.setObjectName("material_product")
        # label_material_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        input_material_product=QLineEdit()
        input_material_product.setObjectName("input_material_product")
        # input_material_product.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_Save=QPushButton("Guardar")
        btn_Save.setObjectName("btn_save")
        


        mainWidget=QWidget()
        mainWidget.setObjectName("main_widget")
        layout=QGridLayout(mainWidget)
        layout.addWidget(image_label,0,0,1,6)
        layout.addWidget(label_name_product,1,1,1,2)
        layout.addWidget(input_name_product,1,3,1,2)
        layout.addWidget(label_marc_product,2,1,1,2)
        layout.addWidget(input_marc_product,2,3,1,2)
        layout.addWidget(label_price_product,3,1,1,2)
        layout.addWidget(spiner_price_product,3,3,1,2)
        layout.addWidget(label_unid_product,4,1,1,2)
        layout.addWidget(unidComboBox,4,3,1,2)
        layout.addWidget(label_size_product,5,1,1,2)
        layout.addWidget(input_size_product,5,3,1,2)
        layout.addWidget(label_color_product,6,1,1,2)
        layout.addWidget(input_color_product,6,3,1,2)
        layout.addWidget(label_date_expire_product,7,1,1,2)
        layout.addWidget(qdate_expire_date_product,7,3,1,2)
        layout.addWidget(label_material_product,8,1,1,2)
        layout.addWidget(input_material_product,8,3,1,2)
        layout.addWidget(btn_Save,9,2,1,2)

         # Crear un layout vertical
               
        # Crear la tabla
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(100)  # Número de filas
        self.table_widget.setColumnCount(10)  # Número de columnas
        labels_table=self.labelsHeaderTable()
        # Llenar la tabla con datos de ejemplo
        for row in range(100):
            for cont in range(0,len(labels_table),1):
                item = QTableWidgetItem(f"Item {row},{cont}")
                self.table_widget.setItem(row, cont, item)
        
        # Crear una área de desplazamiento
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table_widget)
        scroll_area.setWidgetResizable(True)
        
        # Añadir el área de desplazamiento al layout
        layout.addWidget(scroll_area,10,1,1,4)

        self.setLayout(layout)
   
    def optionsComboBox(self):
        return ["unid","paquete","caja","bolsa"]
    
    def labelsHeaderTable(self):
        return ["Nombre","Categoria","Marca","Precio","unid","size","color","expiration_date","material"]

app = QApplication(sys.argv)

app.setStyleSheet(styleProduct())

window = Product()
sys.exit(app.exec())
