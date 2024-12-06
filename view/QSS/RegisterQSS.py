def qssStyleCategory():
    return   """
    QWidget{
    background: linear-gradient(180deg,
    rgba(204,204,204,1) 0%,
    rgba(238,238,238) 50%,
    rgba(204,204,204) 100%);
    
    }
    QLabel, QCheckBox, QPushButton {
        background-color: transparent;
    }
    QLabel#name_local {
        font-size: 26px;
        font-family: Arial;
    }
    
    QLabel#image {
        margin:7%;        
    }
    
    QLineEdit{
       height: 50px; 
       font-size: 16px;
    }
    
    QLabel#name_local {
        font-size: 26px;
        font-family: Arial;
    }
    
    QLabel#type_local{
        font-size: 22px;
        font-family: Arial;
    }
    
    QCheckBox{
        font-size: 17px;
        font-family: Arial;
        margin:8px 2px;
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