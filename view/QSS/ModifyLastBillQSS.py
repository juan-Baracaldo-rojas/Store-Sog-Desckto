def styleCategory():
    return """
    #bill_id{
    font-family:sans-serif;
    font-size:32px;
    }
    #label_id,#cant_sales{
    font-size:22px;

    }
    
        QComboBox,QSpinBox{
    padding:0 12px;
    font-size:22px;
    border: 2px solid #66afe9;
    border-radius: 5px;
    background-color: #f9f9f9;
    color: #333333;
    }
    QPushButton {
        background-color: #4CAF50; /* Verde */
        color: white;
        border: none;
        padding: 10px 20px;
        margin:2px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        margin: 4px 2px;
    }

    QPushButton:hover {
        background-color: #45a049; /* Verde oscuro */
    }
    
    QPushButton:pressed {
        background-color: #3e8e41; /* Verde aún más oscuro */
    }

"""