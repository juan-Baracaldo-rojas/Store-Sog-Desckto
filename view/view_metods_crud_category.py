def MessageCategoryInsertSuccesfull():
    print("Categoría registrada exitosamente.") 

def MessageUpdateCategory():
    print(f'Categoria actualizada')

def seeAllCategories(rows):
    for row in rows:
        print(row)

def MessageIdNotFound():
    print("No se encontro ninguna categoria con ese Id")

def MessageDeleteCategorySuccess():
    print(f'Categoria Eliminada CorrectamentAe')

def MessageDeleteCategory():
    opc=input('\nEsta seguro que desea eliminar la categoria.\n1.Si\n2.No\n')
    return opc

def MessageErrorUpdateCategory(e):
    print(f"Error al actualizar la categoría: {e}")

def MessageErrorSeeAllCategory(e):
    print(f"Error al ver todas las categoría: {e}")

def MessageErrorInsertCategory(e):
    print(f"Error al insertar la categoría: {e}")

def MessageErrorDeleteCategory(e):
    print(f"Error al eliminar la categoría: {e}")
