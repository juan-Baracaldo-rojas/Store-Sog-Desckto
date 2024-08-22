import sys
import os
import sqlite3
import pandas as pd

# Añadir la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from view.View_other_metods import MessageErrorHistorySalesByYear,viewHistorySellByYear,MessageErrorHistorySalesByMonth,viewHistorySellByMonth,MessageErrorHistorySalesByDay,viewHistorySellByDay,MessageErrorBillProductList,MessageErrorProductSearch,ViewProductsSell,MessageErrorSeeBestProducts,MessageErrorSeeListBestProducts,ViewTop10,MessageErrorSeeAllExpireProducts,MessageBestProduct,MessageDowloadFailes,MessageDowloadOption,MessageDowloadSucces,SeeAllDataSearch,viewDataGraficHistogramBestSales,viewDataGraficLineSalesForDay,viewDateBill,SeeAllExpireProductDetailSells
from model.Category import Category
from model.Product import Product
from model.Sell import Sell
from model.SellDetail import SellDetail
from controller.ControllerProducts import all_Products
from controller.ControllerCategory import all_categories

def start():
    print(f'Other Metods')
    
def all_products_invetory_Expire():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Producto WHERE stock_actual>0 and fecha_vencimiento not null;')
        rows=cursor.fetchall()
        SeeAllExpireProductDetailSells(rows)
    except sqlite3.Error as e:
        MessageErrorSeeAllExpireProducts(e)
    finally:
        conn.close()
    
def list_best_products():
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
 
def best_product():
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

def HistorySalesDay(dateReport):
    try:
        conn =sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT p.nombre,de.cantidad,de.precio_unitario,v.Fecha,de.sub_total  FROM Detalle_venta de  JOIN Producto p ON de.id_producto=p.id_producto  JOIN Venta v on de.id_venta=v.id_venta WHERE v.Fecha= ?',(dateReport,))
        rows=cursor.fetchall()
        viewHistorySellByDay(dateReport,rows)
# def dowloadProducts():
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
    rowsSales=HistorySalesDay(date)
    print(f'\n\n\n\nDescargando Ventas de {date}')
    df=pd.DataFrame(rowsSales,columns=["Nombre Producto","Cantidad","Precio Unitario","Fecha","Sub Total"])
    df.to_excel(f'../dowloads/Ventas_{date}.xlsx', index=False)

def DowloadProducts():
    rowsProducts=all_Products()
    print(f'\n\n\n\nDescargando Productos ')
    df=pd.DataFrame(rowsProducts,columns=["Id","Nombre","Categoria","Marca","Precio","Stock Actual","Stock Vendido","Unidad","Tamaño","Color","Fecha de expiracion","Material"])
    df.to_excel('../dowloads/Productos.xlsx', index=False)

def DowloadCategory():
    rowsCategory=all_categories()
    print(f'\n\n\nDescargando Categoria ')
    df=pd.DataFrame(rowsCategory,columns=["Id","Nombre","Descripcion"])
    df.to_excel('../dowloads/Categoria.xlsx', index=False)

def empowermentList():
    return ["Ten una cuenta visible en Google my bussiness","Aparecer en google maps","Usa una red social para crear tu perfil de empresa"]
if __name__ == "__main__":
    start()
    # all_products_invetory_Expire()
    # list_best_products()
    # best_product()
    # searchProductList("ca")
    # BillProductList(1)
    # HistorySalesDay('10-12-2022')
    # HistorySalesMonth('12','2022')
    # HistorySalesYear("2022")
    # DowloadSalesDay('10-12-2022')
    # DowloadProducts()
    # DowloadCategory()