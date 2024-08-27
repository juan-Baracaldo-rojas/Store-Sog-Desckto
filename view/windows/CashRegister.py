import sys
import os
from PyQt6.QtWidgets import QHBoxLayout,QTableWidget,QTableView,QHeaderView, QApplication, QWidget, QDateEdit, QLabel, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from controller.ControllerSell import candySalesCondition,ropeSalesCondition,printerSalesCondition,papelerySalesCondition,toyStoreSalesCondition,shoesStoreSalesCondition
from view.QSS.CashRegisterQSS import styleCashResgister

class CashRegister(QWidget,):
    def resource_path(self, relative_path):
        """Obtiene la ruta absoluta al recurso, trabajando para dev y para PyInstaller"""
        try:
            # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def widgetSearch(self):
        widget_search=QWidget()
        search_layout=QGridLayout(widget_search)

        input_search_word=QLineEdit()
        input_search_word.setObjectName("input_search_word")

        btn_buscar=QPushButton("BUSCAR")
        btn_buscar.setObjectName("btn_buscar")
        search_layout.addWidget(input_search_word,0,1,1,3)
        search_layout.addWidget(btn_buscar,0,4)
        return widget_search
    
    def __init__(self,typeSale):
        self.typeSale=typeSale
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Login')
        # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
        self.setFixedSize( 1200, 810)
        self.generate_form()
        self.show()
    

    def generate_form(self):
       

        


        principal_widget=QWidget()
        principal_layout=QVBoxLayout(principal_widget)

        principal_layout.addWidget(self.widgetTitle())
        principal_layout.addWidget(self.widgetSearch())
        principal_layout.addWidget(self.widgetMenuSearch())
        principal_layout.addWidget(self.widgetResultados())
        principal_layout.addWidget(self.widgedtButom())


        self.setLayout(principal_layout)
    
    def widgetResultados(self):
                # Configurar el diseño para mostrar los resultados de la búsqueda
        widget_resultados = QWidget()
        self.layout_resultados = QVBoxLayout(widget_resultados)

        # Envolver los resultados en un QWidget
        # widget_resultados.setLayout(self.layout_resultados)
        widget_resultados.setFixedSize(1180, 250)  # Establecer tamaño fijo al QWidget

        # Configurar la tabla para mostrar datos de productos
        self.tabla_productos = QTableWidget(self)
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setHorizontalHeaderLabels(["Nombre Producto", "Cantidad", "Precio","Total"])
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
        self.layout_resultados.addWidget(self.tabla_productos)
        
        return widget_resultados
    
    def widgetTitle(self):
        widget_title=QWidget()
        title_layout=QVBoxLayout(widget_title)

        label_title=QLabel("Caja")
        label_title.setObjectName("label_title")
        label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_layout.addWidget(label_title)
        if shoesStoreSalesCondition(self.typeSale):
            image_sales_shoes = QLabel()
            pixmap = QPixmap(self.resource_path('../../Img/ico_zapatos.png'))  # Ruta relativa de la imagen
            image_sales_shoes.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_sales_shoes.setPixmap(pixmap)
            image_sales_shoes.setObjectName("image_sales_shoes") 
            title_layout.addWidget(image_sales_shoes)
        elif papelerySalesCondition(self.typeSale):
            image_sales_papelery = QLabel()
            pixmap = QPixmap(self.resource_path('../../Img/ico_papeleria.png'))  # Ruta relativa de la imagen
            image_sales_papelery.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_sales_papelery.setPixmap(pixmap)
            image_sales_papelery.setObjectName("image_papelery") 
            title_layout.addWidget(image_sales_papelery)
        elif toyStoreSalesCondition(self.typeSale):
            image_toy_store = QLabel()
            pixmap = QPixmap(self.resource_path('../../Img/ico_juguetes.png'))  # Ruta relativa de la imagen
            image_toy_store.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_toy_store.setPixmap(pixmap)
            image_toy_store.setObjectName("image_toy_store") 
            title_layout.addWidget(image_toy_store)
        elif printerSalesCondition(self.typeSale):
            image_printer = QLabel()
            pixmap = QPixmap(self.resource_path('../../Img/ico_impresora.png'))  # Ruta relativa de la imagen
            image_printer.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_printer.setPixmap(pixmap)
            image_printer.setObjectName("image_printer") 
            title_layout.addWidget(image_printer)
        elif ropeSalesCondition(self.typeSale):
            image_rope_sales = QLabel()
            pixmap = QPixmap(self.resource_path('../../Img/ico_ropa.png'))  # Ruta relativa de la imagen
            image_rope_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_rope_sales.setPixmap(pixmap)
            image_rope_sales.setObjectName("image_rope") 
            title_layout.addWidget(image_rope_sales)
        elif candySalesCondition(self.typeSale):
            image_candy_sales = QLabel()
            pixmap = QPixmap(self.resource_path('../../Img/ico_comestible.png'))  # Ruta relativa de la imagen
            image_candy_sales.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_candy_sales.setPixmap(pixmap)
            image_candy_sales.setObjectName("image_candy_sales") 
            title_layout.addWidget(image_candy_sales)
        
        return widget_title
    
    def widgetMenuSearch(self):
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

        return widget_header
    
    def widgedtButom(self):
        widget_buttom=QWidget(self)
        layout_butoms=QGridLayout(widget_buttom)
        
        btn_generate_bill=QPushButton('Crear factura', self)
        btn_generate_bill.setObjectName('btn_create_bill')
        btn_generate_bill.clicked.connect(self.create_bill)


        btn_cancel=QPushButton('Cancelar', self)
        btn_cancel.setObjectName('btn_cancel')
        btn_cancel.clicked.connect(self.cancel)
      
        

        layout_butoms.addWidget(btn_generate_bill,0,0)
        layout_butoms.addWidget(btn_cancel,0,1)
        return widget_buttom

    def mostrar_resultados(self, resultados):
        # Limpiar el diseño de resultados existentes
        for i in reversed(range(self.layout_resultados.count())):
            layout_item = self.layout_resultados.itemAt(i)
            if layout_item is not None:
                for j in reversed(range(layout_item.count())):
                    widget = layout_item.itemAt(j).widget()
                    if widget is not None:
                        widget.setParent(None)

        # Mostrar los resultados en el diseño
        for producto in resultados:
            layout_producto = QHBoxLayout()
            
            label_id = QLabel(str(producto["id_producto"]))
            label_id.setFont(QFont("Arial",12))
            label_id.setFixedSize(40,30)

            label_nombre = QLabel(producto["nombre_producto"])
            label_nombre.setFont(QFont("Arial",12))
            label_nombre.setFixedSize(560,30)
            
            label_num_pedido = QLabel(str(producto["num_pedido"]))
            label_num_pedido.setFont(QFont("Arial",12))
            label_num_pedido.setFixedSize(80,30)
            
            label_fecha_producto = QLabel(str(self.convertFormatDate(producto["fecha_vencimiento"])))
            label_fecha_producto.setFont(QFont("Arial",12))
            label_fecha_producto.setFixedSize(140,30)
             
            spinbox_cantidad = QSpinBox()
            spinbox_cantidad.setMaximum(producto["cant_maxima"])
            spinbox_cantidad.setFixedSize(50,30)

            label_precio = QLabel(str(producto["precio_venta_x_unidad"]))
            label_precio.setFont(QFont("Arial",12))
            label_precio.setFixedSize(140,30)
            label_precio.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            boton_comprar = QPushButton("Comprar")
            boton_comprar.setFixedSize(120,30)
            # TODO ARREGLAR LOS DATOS DE ACA
            
            # Conectar la señal clicked del botón a un método utilizando lambda
            boton_comprar.clicked.connect(lambda _, id=int(label_id.text()),num_pedido=int(label_num_pedido.text()),precio=int(label_precio.text()),nombre_producto=label_nombre.text(),cantidad_spinbox=spinbox_cantidad: self.mostrar_mensaje_compra(id,num_pedido,precio,nombre_producto,int(cantidad_spinbox.value()),producto) )

            layout_producto.addWidget(label_id)
            layout_producto.addWidget(label_nombre)
            layout_producto.addWidget(label_num_pedido)
            layout_producto.addWidget(label_fecha_producto)
            layout_producto.addWidget(spinbox_cantidad)
            layout_producto.addWidget(label_precio)
            layout_producto.addWidget(boton_comprar)

            self.layout_resultados.addLayout(layout_producto)
    def mostrar_mensaje_compra(self, id_producto,num_pedido,precio_unitario,nombre_producto, cantidad_comprada,producto):
         # URL de la API local
        # url = "http://localhost:3001/create_bill_product"
        total=cantidad_comprada*producto['precio_venta_x_unidad']
            # La solicitud fue exitosa
        print("Solicitud exitosa")
            # Hubo un error en la solicitud
        mensaje="" 
        QMessageBox.information(self, "Compra realizada", mensaje)
        self.input.clear()
        self.mostrar_resultados([])
        resultados=self.seeProductsBills()
        self.actualizar_tabla(resultados)
    
    def cancel(self):
        print(f'Cancel')
    def create_bill(self):
        print(f'Cancel')
app = QApplication(sys.argv)
app.setStyleSheet(styleCashResgister())
window = CashRegister("Zapatos")
sys.exit(app.exec())
