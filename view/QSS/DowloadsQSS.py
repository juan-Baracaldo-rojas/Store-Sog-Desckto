def styleDowloads():
    return """
    QLabel{
        font-size:20px;
    }
    QDateEdit{
    padding: 8px 20px;
        margin:auto;
    }
    QPushButton {
        background-color: #fff; 
        border:1px solid #000;
        border-radius:10%;
        color: black;
        padding: 8px 20px;
        margin:auto;
        font-family:sans-serif;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        
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