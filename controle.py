from PyQt5 import uic,QtWidgets

def funcao_principal():
    codigo_produto = formulario_cadastro.lineEdit.text()
    print("Código : ",codigo_produto)
    descricao_produto = formulario_cadastro.lineEdit_2.text()
    print("Descrição : ",descricao_produto)
    codigo_barras = formulario_cadastro.lineEdit_3.text()
    print("Código de barras :",codigo_barras )
    preco_produto = formulario_cadastro.lineEdit_4.text()
    print("Preço : ",preco_produto)
    codigo_ncm = formulario_cadastro.lineEdit_5.text()
    print("NCM : ",codigo_ncm)
    if formulario_cadastro.radioButton.isChecked():
        print("Categoria : Alimentos")
    elif formulario_cadastro.radioButton_2.isChecked():
        print("Categoria : Não Alimento")
    else :
        print("Categoria : Perecíves")



app=QtWidgets.QApplication([])
formulario_cadastro=uic.loadUi("formulario_cadastro.ui")
formulario_cadastro.pushButton.clicked.connect(funcao_principal)

formulario_cadastro.show()
app.exec()