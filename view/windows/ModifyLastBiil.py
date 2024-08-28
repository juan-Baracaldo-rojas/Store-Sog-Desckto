import sys
import os
from PyQt6.QtWidgets import QHBoxLayout,QTableWidget,QTableView,QHeaderView,QComboBox, QApplication, QWidget, QDateEdit, QLabel, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.ModifyLastBillQSS import styleCategory

class ModifyLastBills(QWidget):
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
        self.setWindowTitle('Modificar ultima factura')
        # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
        self.setFixedSize( 1200, 810)
        self.generate_form()
        self.show()

    def generate_form(self):
        principal_widget=QWidget()
        principal_layout=QGridLayout(principal_widget)
        principal_layout.addWidget(self.widgetTitle(),0,0,1,3)
        principal_layout.addWidget(self.widgetForm(),1,0,1,3)
        principal_layout.addWidget(self.widgetListProduct(),2,1)

        self.setLayout(principal_layout)
    
    def widgetTitle(self):
        widget_title=QWidget()
        layout_title=QVBoxLayout(widget_title)
        image_label_category = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico-modify_last_bill.png'))  # Ruta relativa de la imagen
        image_label_category.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_category.setPixmap(pixmap)
        image_label_category.setObjectName("image_category") 
        
        id=1
        label_bill_id=QLabel(f"Identificador ultima Factura {id}")
        label_bill_id.setObjectName("bill_id")
        label_bill_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout_title.addWidget(image_label_category)
        layout_title.addWidget(label_bill_id)

        widget_title.setFixedSize(1100,300)

        return widget_title

    def widgetForm(self):
        widget_form=QWidget()
        layout_form=QGridLayout(widget_form)
        

        id=1
        label_product_id=QLabel(f"Producto")
        label_product_id.setObjectName("label_id")
        label_product_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        productComboBox = QComboBox()
        options=self.optionsComboBox()
        productComboBox.addItems(options)
        
        label_cantidad_sales=QLabel(f"Cantidad a vender")
        label_cantidad_sales.setObjectName("cant_sales")
        label_cantidad_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cant_max=2
        spiner_cant = QSpinBox()
        spiner_cant.setObjectName("spiner_cant")
        spiner_cant.setMaximum(cant_max)
        spiner_cant.setMinimum(0)
        spiner_cant.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        btn_modify=QPushButton("MODIFICAR")
        btn_modify.setObjectName("btn_modify")

        layout_form.addWidget(label_product_id,0,1)
        layout_form.addWidget(productComboBox,0,2,1,3)
        layout_form.addWidget(label_cantidad_sales,1,1)
        layout_form.addWidget(spiner_cant,1,2,1,3)
        layout_form.addWidget(btn_modify,2,2,1,3)
        
        widget_form.setFixedSize(1100,180)
      
        return widget_form
    def widgetListProduct(self):
         # seccion header
        self.label_header_id_producto = QLabel("Id")
        self.label_header_id_producto.setFont(QFont("Arial",12))
        self.label_header_id_producto.setFixedSize(40,30)
        
        self.label_header_nombre_producto = QLabel("Nombre producto")
        self.label_header_nombre_producto.setFont(QFont("Arial",12))
        self.label_header_nombre_producto.setFixedSize(540,30)

        self.label_header_num_pedido = QLabel("Num Pedido")
        self.label_header_num_pedido.setFont(QFont("Arial",12))
        self.label_header_num_pedido.setFixedSize(100,30)
      
        self.label_header_fecha_vencimiento = QLabel("Fecha vencimiento")
        self.label_header_fecha_vencimiento.setFont(QFont("Arial",12))
        self.label_header_fecha_vencimiento.setFixedSize(150,30)

        self.label_header_cantidad = QLabel("Cantidad")
        self.label_header_cantidad.setFont(QFont("Arial",12))
        self.label_header_cantidad.setFixedSize(90,30)
        
        self.label_header_precio = QLabel("Precio Uni")
        self.label_header_precio.setFont(QFont("Arial",12))
        self.label_header_precio.setFixedSize(230,30)

        widget_header=QWidget()
        self.layout_header=QHBoxLayout(widget_header)
        self.layout_header.addWidget(self.label_header_id_producto)
        self.layout_header.addWidget(self.label_header_nombre_producto)
        self.layout_header.addWidget(self.label_header_num_pedido)
        self.layout_header.addWidget(self.label_header_fecha_vencimiento)
        self.layout_header.addWidget(self.label_header_cantidad)
        self.layout_header.addWidget(self.label_header_precio)

        widget_header.setFixedSize(1100,450)
        
        return widget_header

    def optionsComboBox(self):
        return ["opc1","opc2","opc3"]
app = QApplication(sys.argv)
app.setStyleSheet(styleCategory())
window = ModifyLastBills()
window.show()
sys.exit(app.exec())