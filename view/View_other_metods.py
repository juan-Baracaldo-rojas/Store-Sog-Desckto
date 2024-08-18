def SeeAllExpireProductDetailSells(rowsExpireProducts):
    for row in rowsExpireProducts:
        print(row)

def MessageBestProduct(nameProduct):
    print(f'\nEl producto mas vendido es: {nameProduct[0][0]} ')


def MessageDowloadSucces(dateDowload, typeArchive):
    print(f'Se Descago correctamente el archibo {typeArchive}:\nfecha descarga {dateDowload}')

def MessageDowloadFailes(dateDowload, typeArchive):
    print(f'No se pudo descargar el archibo {typeArchive}:\nfecha descarga {dateDowload}')
    
def MessageDowloadOption(typeArchive):
    opc=input(f'\nEsta seguro que desea descargar {typeArchive}  de venta.\n1.Si\n2.No\n')
    return opc

def SeeAllDataSearch(word,rowsProducts):
    print(f'\nSe encontro las siguientes coinciedencias con la palabra {word}\n')
    for row in rowsProducts:
        print(row)

def viewDataGraficHistogramBestSales(RowsBestProducts,RowsTotalSell):
    for cont in range(0,len(RowsBestProducts),1):
        print(f'\n{cont}. Producto: {RowsBestProducts[cont]} \tTotal vendido: {RowsTotalSell[cont]} ')

def viewDataGraficLineSalesForDay(RowsTime,RowsTotalSell):
    for cont in range(0,len(RowsTime),1):
        print(f'\n{cont}. Producto: {RowsTime[cont]} \tTotal vendido: {RowsTotalSell[cont]} ')

def viewDateBill(RowsDataBill):
    for row in RowsDataBill:
        print(row)

def ViewTop10(rowsProducts):
    print(f'\nTop 10\n')
    for row in rowsProducts:
        print(row)
        
def ViewProductsSell(rowsProducts):
    print(f'\nProductos buscadors\n')
    for row in rowsProducts:
        print(row)

def viewHistorySellByDay( dateSell,rowsSales):
    print(f'\nHistoria de  ventas del dia {dateSell}\n')
    for row in rowsSales:
        print(row)

def viewHistorySellByMonth( month, year,rowsSales):
    print(f'\nHistoria de  ventas del mes {month} del año {year}  \n')
    for row in rowsSales:
        print(row)
    

def viewHistorySellByYear( year,rowsSales):
    print(f'\nHistoria de ventas del año {year}  \n')
    for row in rowsSales:
        print(row)
    
# MESSAGES ERROR

def MessageErrorSeeAllExpireProducts(e):
    print(f"Error al ver los productos disponibles: {e}")

def MessageErrorSeeListBestProducts(e):
    print(f"Error al ver top 10: {e}")

def MessageErrorSeeBestProducts(e):
    print(f"Error al ver el mejor producto: {e}")

def MessageErrorProductSearch(search_word,e):
    print(f"Error al ver la lista de producto coincidentes con {search_word}: {e}")

def MessageErrorBillProductList(id_sell,e):
    print(f"Error al ver los producto de la factura {id_sell}: {e}")

def MessageErrorHistorySalesByDay(dateSell,e):
    print(f"Error al ver el historial en el dia {dateSell}: {e}")

def MessageErrorHistorySalesByMonth(month, year,e):
    print(f"Error al ver el historial en el mes {month} en el año {year} : {e}")

def MessageErrorHistorySalesByYear(year,e):
    print(f"Error al ver el historial en el año {year} : {e}")

