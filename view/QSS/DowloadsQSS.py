def styleDowloads():
    return """
    QLabel{
        font-size:20px;
    }
    QDateEdit{
    padding: 15px 20px;
        margin:2px;
    }
    QPushButton {
        background-color: #fff; 
        border:1px solid #000;
        border-radius:10%;
        color: black;
        padding: 15px 20px;
        margin:2px;
        font-family:sans-serif;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        margin: 4px 2px;
        
    }

    QPushButton:hover {
        background-color: #45a049; /* Verde oscuro */
        color: white;
    
    }
    
    QPushButton:pressed {
        color: white;
        background-color: #3e8e41; /* Verde aún más oscuro */
    }
"""