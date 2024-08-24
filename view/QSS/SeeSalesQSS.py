def styleSeeSales():
    return """
    QWidget{
    background-color:#faf6f6 ;
    
    }
    #image_see_sales{
        margin:auto;
        background-color: transparent;
    }

    #customTableWidget {
        background-color: #fff4f3 ;
        gridline-color: #c0c0c0 ;
        font-size: 14px;
        margin: 2px;
        border: 1px solid #c0c0c0;
    }

    #customTableWidget::item {
        padding: 5px;
    }
  

    #customTableWidget QHeaderView::section {
        background-color: rgba(8, 209, 240 ,0.1);
        padding: 4px;
        border: 1px solid #c0c0c0;
    }
    #label_total,#label_date{
        font-size:30px;
        margin:10px;
    }
    QDateEdit{
      width:50%;
        margin: 7px auto;
       font-size: 22px;
    }

      #customDateEdit {
        border: 2px solid #3498db;
        border-radius: 5px;
        padding: 5px;
        background-color: #ecf0f1;
        color: #2c3e50;
    }

    #customDateEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left: 1px solid #3498db;
    }

    #customDateEdit::down-arrow {
        image: url(down_arrow.png);  /* Reemplaza con la ruta de tu imagen */
        width: 10px;
        height: 10px;
    }

    #customDateEdit QAbstractItemView {
        background-color: #ecf0f1;
        selection-background-color: #3498db;
        selection-color: white;
    }
"""