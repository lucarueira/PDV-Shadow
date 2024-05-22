from PyQt5 import uic,QtWidgets
import mysql.connector
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastro_produtos"
)

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

    categoria = ""

    if formulario_cadastro.radioButton.isChecked():
        print("Categoria : Alimentos")
        categoria= "Alimentos"
    elif formulario_cadastro.radioButton_2.isChecked():
        print("Categoria : Não Alimento")
        categoria = "Não Alimento"
    else :
        print("Categoria : Perecíves")
        categoria = "Perecíveis"

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,codigodebarras,preco,ncm,categoria) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (str(codigo_produto),str(descricao_produto),str(codigo_barras),str(preco_produto),str(codigo_ncm),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    




app=QtWidgets.QApplication([])
formulario_cadastro=uic.loadUi("formulario_cadastro.ui")
formulario_cadastro.pushButton.clicked.connect(funcao_principal)

formulario_cadastro.show()
app.exec()



