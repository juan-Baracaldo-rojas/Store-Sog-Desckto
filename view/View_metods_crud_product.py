def MessageProductInsertSuccesfull():
    print("Producto registrado exitosamente.") 

def MessageUpdateProduct():
    print(f'Producto actualizado')

def ViewSeeAllProducts(rows):
    for row in rows:
        print(row)

def MessageIdNotFound():
    print("No se encontro ningun Producto con ese Id")

def MessageDeleteProductSuccess():
    print(f'Producto Eliminado Correctamente')

def MessageDeleteProduct():
    opc=input('\nEsta seguro que desea eliminar el Producto.\n1.Si\n2.No\n')
    return opc

def MessageErrorUpdateProduct(e):
    print(f"Error al actualizar la Producto: {e}")

def MessageErrorSeeAllProduct(e):
    print(f"Error al ver todas las Producto: {e}")

def MessageErrorInsertProduct(e):
    print(f"Error al registrar la Producto: {e}")

def MessageErrorDeleteProduct(e):
    print(f"Error al eliminar la Producto: {e}")
