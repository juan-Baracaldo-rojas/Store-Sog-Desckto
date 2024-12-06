def styleProduct():
    return """
    QWidget{
    background: linear-gradient(180deg,
    rgba(204,204,204,1) 0%,
    rgba(238,238,238) 50%,
    rgba(204,204,204) 100%);
    
    }

    QLabel#image{
       margin:0;
       padding:0;
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
        margin: 4px 2px 4px 20px;
    }

    QPushButton:hover {
        background-color: #45a049; /* Verde oscuro */
    }
    
    QPushButton:pressed {
        background-color: #3e8e41; /* Verde aún más oscuro */
    }


    QLabel{
        font-size: 16px;
    }
    QLineEdit,QDateEdit,QComboBox,QSpinBox{
       height: 20px; 
       font-size: 16px;
       padding:2px;
    }
"""