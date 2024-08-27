def styleGrafics():
    return """
QLabel{
    font-family:sans serif;
    font-size:20px;
    }
  QDateEdit, QSpinBox, QComboBox {
    font-size: 20px;
    padding: 5px;
    border: 2px solid #66afe9;
    border-radius: 5px;
    background-color: #f9f9f9;
    color: #333333;
    min-height: 30px;
}


QDateEdit:hover, QSpinBox:hover, QComboBox:hover {
    border: 2px solid #b3b3b3;
}

QComboBox::drop-down {
    width: 30px;
}
#info{
   background-color: #d7e9ed ;
    
}

QSpinBox::up-button, QSpinBox::down-button {
    width: 20px;
    height: 20px;
}

QDateEdit::drop-down {
    border-left: 1px solid #cccccc;
}
"""