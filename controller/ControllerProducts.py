import sys
import os
import sqlite3

# Añadir la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.Product import Product
from view.View_metods_crud_product import MessageDeleteProduct,MessageDeleteProductSuccess,MessageErrorDeleteProduct,MessageErrorInsertProduct,MessageErrorSeeAllProduct,MessageErrorUpdateProduct,MessageIdNotFound,MessageProductInsertSuccesfull,MessageUpdateProduct,ViewSeeAllProducts

def start():
    print(f'Controller Sell')

# CRUD CATEGORY

def insert_product(product):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO producto (nombre,categoria,marca,precio,stock_actual,stock_vendido,unidad,talla,color,fecha_vencimiento,material) VALUES (?,?,?,?,?,?,?,?,?,?,?)
        ''', (product.name,product.category,product.marca,product.price,product.stock_actual,product.stock_sell,product.unid,product.size,product.color,product.expiration_date,product.material))
        
        conn.commit()
        MessageProductInsertSuccesfull()
    except sqlite3.Error as e:
        MessageErrorInsertProduct(e)
    finally:
        # Cerrar la conexión
        conn.close()


def update_product(product,id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
             UPDATE producto
            SET nombre=?,
            categoria=?,
            marca=?,
            precio=?,
            stock_actual=?,
            stock_vendido=?,
            unidad=?,
            talla=?,
            color=?,
            fecha_vencimiento=?,
            material=?
            WHERE Id_producto = ?
        ''', (product.name,product.category,product.marca,product.price,product.stock_actual,product.stock_sell,product.unid,product.size,product.color,product.expiration_date,product.material,id))
  
        
        conn.commit()
        MessageUpdateProduct()
       
    except sqlite3.Error as e:
        MessageErrorUpdateProduct(e)
    finally:
        conn.close() 


def delete_product(id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        opc=MessageDeleteProduct()
        if opc=='1':
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM producto
                WHERE Id_producto = ?
            ''', (id,))
            conn.commit()
            if cursor.rowcount > 0:
                MessageDeleteProductSuccess()
            else:
                MessageIdNotFound()
       
    except sqlite3.Error as e:
        MessageErrorUpdateProduct(e)
    finally:
        conn.close()

def all_Products():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM producto')
        rows=cursor.fetchall()
        ViewSeeAllProducts(rows)
    except sqlite3.Error as e:
        MessageErrorSeeAllProduct(e)
    finally:
        conn.close()
        return rows


if __name__ == "__main__":
    start()
    # product=Product('10-12-2022',99999)
    product = Product("Dulces","Comestibles", "colombina", 29.99,  100,  50,  "unidad", "No_Aplica", "Azul", "10-12-2023",  "Poliéster"  )
    # Llamar a la función de inserción
    insert_product(product)
    # update_product(product,2)
    # delete_product(2)
    # all_Sales()