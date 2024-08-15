def MessageSellInsertSuccesfull():
    print("Venta registrada exitosamente.") 

def MessageUpdateSell():
    print(f'Venta actualizada')

def seeAllSales(rows):
    for row in rows:
        print(row)

def MessageIdNotFound():
    print("No se encontro ninguna Venta con ese Id")

def MessageDeleteSellSuccess():
    print(f'Venta Eliminada Correctamente')

def MessageDeleteSell():
    opc=input('\nEsta seguro que desea eliminar la Venta.\n1.Si\n2.No\n')
    return opc

def MessageErrorUpdateSell(e):
    print(f"Error al actualizar la venta: {e}")

def MessageErrorSeeAllSell(e):
    print(f"Error al ver todas las venta: {e}")

def MessageErrorInsertSell(e):
    print(f"Error al registrar la venta: {e}")

def MessageErrorDeleteSell(e):
    print(f"Error al eliminar la venta: {e}")
