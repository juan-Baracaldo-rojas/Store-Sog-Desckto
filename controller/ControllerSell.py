import sys
import os
import sqlite3

# Añadir la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.Product import Product
from model.Sell import Sell
from model.SellDetail import SellDetail
from view.View_metods_crud_sell import MessageDeleteSell,MessageDeleteSellSuccess,MessageErrorDeleteSell,MessageErrorInsertSell,MessageErrorSeeAllSell,MessageErrorUpdateSell,MessageIdNotFound,MessageSellInsertSuccesfull,MessageUpdateSell,seeAllSales


def start():
    print(f'Controller Sell')

# CRUD CATEGORY

def insert_sell(sell):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO venta (Fecha,Total) VALUES (?,?)
        ''', (sell.sell_date,sell.sell_total))
        
        conn.commit()
        MessageSellInsertSuccesfull()
    except sqlite3.Error as e:
        MessageErrorInsertSell(e)
    finally:
        # Cerrar la conexión
        conn.close()


def update_sell(sell,id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
             UPDATE venta
            SET Fecha = ?,
            total= ?
            WHERE Id_venta = ?
        ''',(sell.sell_date,sell.sell_total,id))
        
        conn.commit()
        MessageUpdateSell()
       
    except sqlite3.Error as e:
        MessageErrorUpdateSell(e)
    finally:
        conn.close() 


def delete_Sell(id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        opc=MessageDeleteSell()
        if opc=='1':
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM venta
                WHERE Id_venta = ?
            ''', (id,))
            conn.commit()
            if cursor.rowcount > 0:
                MessageDeleteSellSuccess()
            else:
                MessageIdNotFound()
       
    except sqlite3.Error as e:
        MessageErrorUpdateSell(e)
    finally:
        conn.close()

def see_all_Sales():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM venta')
        rows=cursor.fetchall()
        seeAllSales(rows)
    except sqlite3.Error as e:
        MessageErrorSeeAllSell(e)
    finally:
        conn.close()

def optionSell():
    return ["Papeleria","Jugueteria","Impresiones","Ropa","Comestibles","Zapatos"] 

def papelerySalesCondition(type_sales):
    return type_sales == "Papeleria"

def toyStoreSalesCondition(type_sales):
    return type_sales == "Jugueteria"

def printerSalesCondition(type_sales):
    return type_sales == "Impresiones"

def ropeSalesCondition(type_sales):
    return type_sales == "Ropa"

def candySalesCondition(type_sales):
    return type_sales == "Comestibles"

def shoesStoreSalesCondition(type_sales):
    return type_sales == "Zapatos"


if __name__ == "__main__":
    start()
    sell=Sell('10-12-2022',99999)
    # Llamar a la función de inserción
    insert_sell(sell)
    # update_sell(sell,2)
    # delete_Sell(2)
    see_all_Sales()