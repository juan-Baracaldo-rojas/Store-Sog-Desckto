import sys
import os
import sqlite3
import pandas as pd
import random

# Añadir la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.View_other_metods import MessageErrorHistorySalesByYear,viewHistorySellByYear,MessageErrorHistorySalesByMonth,viewHistorySellByMonth,MessageErrorHistorySalesByDay,viewHistorySellByDay,MessageErrorBillProductList,MessageErrorProductSearch,ViewProductsSell,MessageErrorSeeBestProducts,MessageErrorSeeListBestProducts,ViewTop10,MessageErrorSeeAllExpireProducts,MessageBestProduct,MessageDowloadFailes,MessageDowloadOption,MessageDowloadSucces,SeeAllDataSearch,viewDataGraficHistogramBestSales,viewDataGraficLineSalesForDay,viewDateBill,SeeAllExpireProductDetailSells,MessageErrorUpdateUser,MessageUpdateUser
from model.Category import Category
from model.Product import Product
from model.Sell import Sell
from model.SellDetail import SellDetail
from controller.ControllerProducts import all_Products
from controller.ControllerCategory import all_categories

def start():
    print(f'Other Metods')
    
def all_products_invetory_Expire():
    rows=[]
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT id_producto,nombre,stock_actual as cantidad_disponible,fecha_vencimiento FROM Producto WHERE stock_actual>0 and fecha_vencimiento not null;')
        rows=cursor.fetchall()
        SeeAllExpireProductDetailSells(rows)
    except sqlite3.Error as e:
        MessageErrorSeeAllExpireProducts(e)
    finally:
        conn.close()
        return rows
    
def list_best_products():
    rows=[]
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT p.nombre,sum(de.sub_total) FROM Detalle_venta as de JOIN Producto as p on de.id_producto= p.id_producto LIMIT 10; ')
        rows=cursor.fetchall()
        ViewTop10(rows)
    except sqlite3.Error as e:
        # print(e)
        MessageErrorSeeListBestProducts(e)
    finally:
        conn.close()
        return rows

def best_product():
    rows=[]
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT p.nombre,sum(de.sub_total) FROM Detalle_venta as de JOIN Producto as p on de.id_producto= p.id_producto LIMIT 1; ')
        rows=cursor.fetchall()
        MessageBestProduct(rows)
    except sqlite3.Error as e:
        # print(e)
        MessageErrorSeeBestProducts(e)
    finally:
        conn.close()
        return rows
 
def searchProductList(search_word):
    try:
        
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('''
            SELECT p.id_producto, p.nombre, p.stock_actual AS "cantidad_max", p.precio AS "precio_unidad"
            FROM Producto p
            WHERE p.stock_actual > 0 AND p.nombre LIKE ?
        ''', (search_word + '%',))
        rows=cursor.fetchall()
        SeeAllDataSearch(search_word,rows)
    except sqlite3.Error as e:
        print(e)
        MessageErrorProductSearch(search_word,e)
    finally:
        conn.close()

def BillProductList(id_sell):
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT p.nombre,de.cantidad,de.precio_unitario,de.sub_total  FROM Detalle_venta de  JOIN Producto p ON de.id_producto=p.id_producto WHERE de.id_venta = ?',
                       (str(id_sell)))
        rows=cursor.fetchall()
        ViewProductsSell(rows)
    except sqlite3.Error as e:
        MessageErrorBillProductList(id_sell,e)
    finally:
        conn.close()

def numberMonth(month):
    numero=0
    if "Enero" == month:
        numero=1
    if "Febrero" == month:
        numero=2
    if "Marzo" == month:
        numero=3
    if "Abril" == month:
        numero=4
    if "Mayo" == month:
        numero=5
    if "Junio" == month:
        numero=6
    if "Julio" == month:
        numero=7
    if "Agosto" == month:
        numero=8
    if "Septiembre" == month:
        numero=9
    if "Octubre" == month:
        numero=10
    if "Noviembre" == month:
        numero=11
    if "Diciembte" == month:
        numero=12
    return numero

def dataGraficLineHistorySalesDaily(dateReport):
    rows=[]
    try:
        conn =sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT v.Fecha,sum(v.total) as total_dia FROM  Venta v  WHERE v.Fecha= ?',(dateReport,))
        rows=cursor.fetchall()
        viewHistorySellByDay(dateReport,rows)
    except sqlite3.Error as e:
        MessageErrorHistorySalesByDay(dateReport,e)
    finally:
        conn.close()
        return rows

def dataGraficLineHistorySalesMonth(month,year):
    rows=[]
    try:
        conn=sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('''
                SELECT 
                       DISTINCT substr(v.Fecha, 1,2) AS dia,
                       sum(v.total) as total_dia   
                FROM  Venta v   
                WHERE substr(v.Fecha, 4,2) = ? and substr(v.Fecha, 7, 4)  =?; 
                     ''',(month,year))
        rows=cursor.fetchall()
        viewHistorySellByMonth(month,year,rows)
    except sqlite3.Error as e:
        MessageErrorHistorySalesByMonth(month,year,e)
    finally:
        conn.close()
        return rows
    
def dataGraficLineHistorySalesYear(year):
    rows=[]
    try:
        conn=sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute("""
            SELECT 
                DISTINCT substr(v.Fecha, 4,2) AS mes,  
                   sum (v.total)	
            FROM  Venta v 
            WHERE substr(v.Fecha, 7, 4)  =?;
                       """,(year,))
        rows=cursor.fetchall()
        viewHistorySellByYear(year,rows)
    except sqlite3.Error as e:
        MessageErrorHistorySalesByYear(year,e)
    finally:
        conn.close()
        return rows
    
def HistorySalesDay(dateReport):
    rows=[]
    try:
        conn =sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT p.nombre,de.cantidad,de.precio_unitario,v.Fecha,de.sub_total  FROM Detalle_venta de  JOIN Producto p ON de.id_producto=p.id_producto  JOIN Venta v on de.id_venta=v.id_venta WHERE v.Fecha= ?',(dateReport,))
        rows=cursor.fetchall()
        viewHistorySellByDay(dateReport,rows)

    except sqlite3.Error as e:
        MessageErrorHistorySalesByDay(dateReport,e)
    finally:
        conn.close()
        return rows

def HistorySalesMonth(month,year):
    try:
        conn=sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('''
               SELECT 
               	p.nombre,
               	de.cantidad,
               	de.precio_unitario,
               	v.Fecha,
               	de.sub_total,
                   substr(v.Fecha, 4,2) AS mes,  
                   substr(v.Fecha, 7, 10) AS anio  
               FROM Detalle_venta de
               JOIN Venta v ON de.id_venta = v.id_venta
               JOIN Producto p ON de.id_producto=p.id_producto
               WHERE substr(v.Fecha, 4,2) = ? and substr(v.Fecha, 7, 4)  =?;
                     ''',(month,year))
        rows=cursor.fetchall()
        viewHistorySellByMonth(month,year,rows)
    except sqlite3.Error as e:
        MessageErrorHistorySalesByMonth(month,year,e)
    finally:
        conn.close()
        
def HistorySalesYear(year):
    try:
        conn=sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute("""
            SELECT 
            	p.nombre,
            	de.cantidad,
            	de.precio_unitario,
            	v.Fecha,
            	de.sub_total,
                substr(v.Fecha, 4,2) AS mes,  
                substr(v.Fecha, 7, 10) AS anio  
            FROM Detalle_venta de
            JOIN Venta v ON de.id_venta = v.id_venta
            JOIN Producto p ON de.id_producto=p.id_producto
            WHERE substr(v.Fecha, 7, 4)  =?;
                       """,(year,))
        rows=cursor.fetchall()
        viewHistorySellByYear(year,rows)
    except sqlite3.Error as e:
        MessageErrorHistorySalesByYear(year,e)
    finally:
        conn.close()

def DowloadSalesDay(date):
    # Definir el directorio donde deseas guardar el archivo
    output_directory = '../../downloads'

    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Ahora puedes guardar tu archivo en este directorio
    file_path = os.path.join(output_directory, f'Ventas_{date}.xlsx')
    rowsSales=HistorySalesDay(date)
    print(f'\n\n\n\nDescargando Ventas de {date}')
    df=pd.DataFrame(rowsSales,columns=["Nombre Producto","Cantidad","Precio Unitario","Fecha","Sub Total"])
    df.to_excel(file_path, index=False)

def DowloadProducts():
    # Definir el directorio donde deseas guardar el archivo
    output_directory = '../../downloads'

    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Ahora puedes guardar tu archivo en este directorio
    file_path = os.path.join(output_directory, 'Productos.xlsx')
    rowsProducts=all_Products()
    print(f'\n\n\n\nDescargando Productos ')
    df=pd.DataFrame(rowsProducts,columns=["Id","Nombre","Categoria","Marca","Precio","Stock Actual","Stock Vendido","Unidad","Tamaño","Color","Fecha de expiracion","Material"])
    df.to_excel(file_path, index=False)

def DowloadCategory():
    # Definir el directorio donde deseas guardar el archivo
    output_directory = '../../downloads'

    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

     # Ahora puedes guardar tu archivo en este directorio
    file_path = os.path.join(output_directory, 'Categoria.xlsx')
    rowsCategory=all_categories()
    print(f'\n\n\nDescargando Categoria ')
    df=pd.DataFrame(rowsCategory,columns=["Id","Nombre","Descripcion"])
    df.to_excel(file_path, index=False)

def empowermentList():
    return ["Ten una cuenta visible en Google my bussiness","Aparecer en google maps","Usa una red social para crear tu perfil de empresa"]

def optionsComboBoxGrafics():
    return  ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembte"]

def columnHeaderTableSeeSales():
    return ["Nombre","Cantidad a vencer","Preciuo Unidad","Fecha","Subtotal" ]

def columHeaderTableProductsExpiration():\
    return ["Id_producto","Nombre","Cantidad","Fecha_vencimiento" ]

def update_user(user):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE local SET 
                    nombre=? ,
                    tipo1=? ,
                    tipo2=? ,
                    tipo3=?             
''',
          (user.name,user.type_1,user.type_2,user.type_3))
  
        
        conn.commit()
        MessageUpdateUser()
       
    except sqlite3.Error as e:
        MessageErrorUpdateUser(e)
    finally:
        conn.close() 

def colorGenerator(cant):
    listColor=[]
    for cont in range(0,cant,1):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        listColor.append((r,g,b))
        print(f'color {cont}')
        print(f'({r},{g},{b})')
    return listColor
if __name__ == "__main__":
    start()
    # all_products_invetory_Expire()
    # print(f'{list_best_products()}')
    # print(dataGraficLineHistorySalesDaily('10-12-2022')); 
    # print(dataGraficLineHistorySalesMonth('12','2022')); 
    # print(dataGraficLineHistorySalesYear('2022')); 
    # colorGenerator(4)
    # print(best_product())
    # searchProductList("ca")
    # BillProductList(1)
    # HistorySalesDay('10-12-2022')
    # HistorySalesMonth('12','2022')
    # HistorySalesYear("2022")
    # DowloadSalesDay('10-12-2022')
    # DowloadProducts()
    # DowloadCategory()