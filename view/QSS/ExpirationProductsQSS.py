def styleExpirationProduct():
    return """
QLabel{
    font-size:30px;
}
#image_see_sales{   
    margin:15px;
}
    #expire_products_table {
        gridline-color: #c0c0c0 ;
        font-size: 14px;
        margin: 2px;
        border: 1px solid #c0c0c0;
    }

    #expire_products_table::item {
        padding: 5px;
    }
  

    #expire_products_table QHeaderView::section {
        background-color: rgba(8, 209, 240 ,0.1);
        padding: 4px;
        border: 1px solid #c0c0c0;
    }
"""