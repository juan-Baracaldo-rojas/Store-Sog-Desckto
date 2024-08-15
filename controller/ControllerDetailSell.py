import sys
import os
import sqlite3

# Añadir la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.SellDetail import SellDetail
from view.View_metods_crud_detail_sell import MessageDeleteDetailSell,MessageDeleteDetailSellSuccess,MessageDetailSellInsertSuccesfull,MessageErrorDeleteDetailSell,MessageErrorInsertDetailSell,MessageErrorSeeAllDetailSell,MessageErrorUpdateDetailSell,MessageIdNotFound,MessageUpdateDetailSell,ViewSeeAllDetailSells

def start():
    print(f'Controller Sell')

# CRUD CATEGORY

def insert_detaill_sell(detail_sell):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO detalle_venta (id_venta,id_producto,cantidad,precio_unitario,sub_total) VALUES (?,?,?,?,?)
        ''', (detail_sell.sell_ID,detail_sell.product_ID,detail_sell.cant,detail_sell.unid_price,detail_sell.subTotal))
        
        conn.commit()
        MessageDetailSellInsertSuccesfull()
    except sqlite3.Error as e:
        MessageErrorInsertDetailSell(e)
    finally:
        # Cerrar la conexión
        conn.close()


def update_detail_sell(detail_sell,sell_ID,product_Id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
             UPDATE detalle_venta SET  cantidad=?, precio_unitario=?, sub_total=? WHERE Id_producto = ? and id_venta=?''',
          (detail_sell.cant,detail_sell.unid_price,detail_sell.subTotal,product_Id,sell_ID))
  
        
        conn.commit()
        MessageUpdateDetailSell()
       
    except sqlite3.Error as e:
        MessageErrorUpdateDetailSell(e)
    finally:
        conn.close() 


def delete_detail_product(product_ID,sell_ID):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        opc=MessageDeleteDetailSell()
        if opc=='1':
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM detalle_venta
                WHERE Id_producto = ? and id_venta=?
            ''', (product_ID,sell_ID))
            conn.commit()
            if cursor.rowcount > 0:
                MessageDeleteDetailSellSuccess()
            else:
                MessageIdNotFound()
       
    except sqlite3.Error as e:
        MessageErrorDeleteDetailSell(e)
    finally:
        conn.close()

def see_all_detail_sell():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM detalle_venta')
        rows=cursor.fetchall()
        ViewSeeAllDetailSells(rows)
    except sqlite3.Error as e:
        MessageErrorSeeAllDetailSell(e)
    finally:
        conn.close()



if __name__ == "__main__":
    start()
    # product=Product('10-12-2022',99999)
    detail_sell = SellDetail(1,1,2,1000)
    # Llamar a la función de inserción
    # insert_detaill_sell(detail_sell)
    # update_detail_sell(detail_sell,1,1)
    delete_detail_product(1,1)
    see_all_detail_sell()