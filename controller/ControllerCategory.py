import sys
import os
import sqlite3


# Añadir la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from view.view_metods_crud_category import MessageDeleteCategorySuccess,MessageErrorDeleteCategory,MessageIdNotFound,MessageDeleteCategory,MessageErrorUpdateCategory,MessageCategoryInsertSuccesfull,MessageErrorInsertCategory,seeAllCategories,MessageErrorSeeAllCategory,MessageUpdateCategory,MessageDeleteCategory
from model.Category import Category
from model.Product import Product
from model.Sell import Sell
from model.SellDetail import SellDetail

def start():
    print(f'Metodo run')

# CRUD CATEGORY

def insert_category(category):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Categoria (Nombre,descripcion) VALUES (?,?)
        ''', (category.name,category.description))
        
        conn.commit()
       
    except sqlite3.Error as e:
        MessageErrorInsertCategory(e)
    finally:
        # Cerrar la conexión
        conn.close()


def update_category(category,id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
             UPDATE categoria
            SET nombre = ?,
            descripcion= ?
            WHERE id = ?
        ''', (category.name,category.description,id))
        
        conn.commit()
        MessageUpdateCategory()
       
    except sqlite3.Error as e:
        MessageErrorUpdateCategory(e)
    finally:
        conn.close() 


def delete_category(id):
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
    
    try:
        opc=MessageDeleteCategory()
        if opc=='1':
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM categoria
                WHERE id = ?
            ''', (id,))
            conn.commit()
            if cursor.rowcount > 0:
                MessageDeleteCategorySuccess()
            else:
                MessageIdNotFound()
       
    except sqlite3.Error as e:
        MessageErrorUpdateCategory(e)
    finally:
        conn.close()

def see_all_categories():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'DB_Store_sog.db')))
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Categoria')
        rows=cursor.fetchall()
        seeAllCategories(rows)
    except sqlite3.Error as e:
        MessageErrorSeeAllCategory(e)
    finally:
        conn.close()



if __name__ == "__main__":
    start()
    # category=Category('Ropa','Categoria')
    # Llamar a la función de inserción
    # insert_category(category)
    # update_category(category,2)
    # delete_category(6)
    # see_all_categories()