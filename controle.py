from PyQt5 import uic,QtWidgets
import mysql.connector



banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastro_produtos"
)

def tela_login():
        formulario_cadastro.show()


def tela_cadastro():
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
    formulario_cadastro.lineEdit.setText("")
    formulario_cadastro.lineEdit_2.setText("")
    formulario_cadastro.lineEdit_3.setText("")
    formulario_cadastro.lineEdit_4.setText("")
    formulario_cadastro.lineEdit_5.setText("")
    formulario_cadastro.radioButton.setCheckable(False)
def formulario_voltar():
    formulario_cadastro.close()

def tela_lista():
    lista_produtos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    lista_produtos.tableWidget.setRowCount(len(dados_lidos))
    lista_produtos.tableWidget.setColumnCount(7)

    for i in range(0,len(dados_lidos)):
        for j in range(0,7):
            lista_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def excluir_dados():
    linha = lista_produtos.tableWidget.currentRow()
    lista_produtos.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))

def lista_voltar():
    lista_produtos.close()

def editar_voltar():
    editar_produto.close()

def tela_editar():
    linha = lista_produtos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
    produto = cursor.fetchall()

    editar_produto.show()

    editar_produto.lineEdit_7.setText(str(produto[0][0]))
    editar_produto.lineEdit.setText(str(produto[0][1]))
    editar_produto.lineEdit_2.setText(str(produto[0][2]))
    editar_produto.lineEdit_3.setText(str(produto[0][3]))
    editar_produto.lineEdit_4.setText(str(produto[0][4]))
    editar_produto.lineEdit_5.setText(str(produto[0][5]))
    editar_produto.lineEdit_6.setText(str(produto[0][6]))
def salvar_editar():
    print("teste")

    

app=QtWidgets.QApplication([])
formulario_cadastro = uic.loadUi("formulario_cadastro.ui")
formulario_cadastro.pushButton.clicked.connect(tela_cadastro)
formulario_cadastro.pushButton_3.clicked.connect(tela_lista)
formulario_cadastro.pushButton_2.clicked.connect(formulario_voltar)

login = uic.loadUi("tela_login.ui")
login.pushButton.clicked.connect(tela_login)

lista_produtos = uic.loadUi("listar_dados.ui")
lista_produtos.pushButton_7.clicked.connect(excluir_dados)
lista_produtos.pushButton_5.clicked.connect(lista_voltar)

editar_produto = uic.loadUi("editar_produtos.ui")
lista_produtos.pushButton_9.clicked.connect(tela_editar)
editar_produto,pushButton.clicked.connect(salvar_editar)
editar_produto.pushButton_2.clicked.connect(editar_voltar)

login.show()
app.exec()



