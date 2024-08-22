def styleSalesMenuQSS():
    return """

      QComboBox{
        width:80%;
        margin:0 auto;
        padding: 15px;
        font-size: 20px;
      }

      QLabel{
        font-size:22px;
      }  

      QPushButton {
        width:80%;
        background-color: #4CAF50; /* Verde */
        color: white;
        border: none;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        font-size: 30px;
        margin: 1px auto;
    }

    QPushButton:hover {
        background-color: #45a049; /* Verde oscuro */
    }
    
    QPushButton:pressed {
        background-color: #3e8e41; /* Verde aún más oscuro */
    }
"""