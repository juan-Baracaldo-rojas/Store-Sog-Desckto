def MessageDetailSellInsertSuccesfull():
    print("detalle de venta registrada exitosamente.") 

def MessageUpdateDetailSell():
    print(f'Detalle de venta actualizado')

def ViewSeeAllDetailSells(rows):
    for row in rows:
        print(row)

def MessageIdNotFound():
    print("No se encontro ningun Detalle con ese Id")

def MessageDeleteDetailSellSuccess():
    print(f'Detalle de venta Eliminado Correctamente')

def MessageDeleteDetailSell():
    opc=input('\nEsta seguro que desea eliminar este detalle de venta.\n1.Si\n2.No\n')
    return opc

def MessageErrorUpdateDetailSell(e):
    print(f"Error al actualizar Detalle de venta: {e}")

def MessageErrorSeeAllDetailSell(e):
    print(f"Error al ver todas las Detalle de venta: {e}")

def MessageErrorInsertDetailSell(e):
    print(f"Error al registrar la Detalle de venta: {e}")

def MessageErrorDeleteDetailSell(e):
    print(f"Error al eliminar la Detalle de venta: {e}")
