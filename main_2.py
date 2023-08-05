from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame)
from ui_main import Ui_MainWindow
from PySide6.QtGui import QIcon
import sys
from PyQt6 import QtCore
from PySide6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from PySide6.QtWidgets import *
from PySide6 import QtCore
from ui_login import Ui_login
import locale
import sys
import locale
import pandas as pd
from PyQt6.QtCore import Qt
import pandas as pd
from PySide6 import QtCore
from PySide6.QtGui import ( QColor, QFont, QIcon)
from PySide6.QtWidgets import *
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_splash_screen import Ui_SplashScreen
from ui_login import Ui_login
import os
from datetime import datetime, timedelta
import locale


########################################  DATAS  ###############################################

# Definir localização para o idioma português
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Obter a data atual
data_atual = datetime.now()

data_hoje = data_atual.strftime('%Y-%m-01')


mes_seguinte = data_atual.replace(month=data_atual.month % 12 + 1)

# Último dia do mês
ultimo_dia_mes = (data_atual.replace(day=1, month=data_atual.month % 12 + 1) - timedelta(days=1)).day

mes_seguinte = mes_seguinte.strftime('%Y-%m-01')

##############################################################################################

## ==> GLOBALS
counter = 0

nome_usuario_log = []

nome_unidade_log = []

nome_departamento_log = []


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)



        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>SEJA BEM VINDO! </strong>")

        # # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>CARREGANDO</strong> BANCO DE DADOS"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>CARREGANDO</strong> INTERFACE"))
        
    
        self.show()
            
      
        

    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
                
        if counter == 50:
            ...
            # COLOCAR VALIDADOR ANTES DE ENTRAR NO LOGIN
               
                
        if counter > 100:        
            # STOP TIMER
            self.timer.stop()
        
                
            # SHOW MAIN WINDOW
            self.main = Login()
            self.main.show()
            self.close()
        
    
            self.close()
            

            

        # INCREASE COUNTER
        counter += 1



# TELA DO LOGIN
class Login(QMainWindow, Ui_login):
    def __init__(self):
        # CODIGO PADRAO Qtdesigner
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login </>")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        
        # quando o botao ENTRAR é clicado, chama a funcao open_system
        self.btn_login.clicked.connect(self.open_system)

        
    
    def open_system(self):

        username = str(self.txt_usuario.text())
        
        password = (self.txt_senha.text())
      
        print(password)
      

        try:
            
            # Colocar um validador do banco de dados, 
            if password == '123':    
                # vai ir para a tela principal do software
                self.window = MainWindow()
                self.window.show()   
                app.exec()
                self.close()
                

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Arcano")
                msg.setText("Usuário ou senha incorreto !\n ! Usuario e senha são os mesmos do login do computador !")
                msg.exec()
                return False
           

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Arcano")
            msg.setText("Usuário ou senha incorreto\n !")
            msg.exec()
            return False


# TELA PRINCIPAL
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # CODIGO PADRAO Qtdesigner
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ARCANO </>")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
            
        
        # Leva para a pagina de noticias ao clicar no botao btn_logo leva para a page
        self.btn_logo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))

        # ao cliclar no btn_menu leva para a função leftmenu
        self.btn_menu.clicked.connect(self.leftMenu)
        
        ## ao clicar no botao btn_metas leva para  page metas
        self.btn_metas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_meta))
        # Dentro possui o btn salvar a planilha 
        self.btn_exportar.clicked.connect(self.salvar)
        # btn limpar o campo de atualização de status do programa
        self.btn_limpar.clicked.connect(self.limpar)
        
        ## Consultar os dados que possui no banco, depois que inseriou a tabela, se for preciso 
        self.btn_consulta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        ## Dentro possui o btn para filtrar
        self.btn_filtro.clicked.connect(self.consultar)
        ## Dentro possui o btn para gerar o excel 
        self.btn_excel.clicked.connect(self.gerar_excel)
        
        self.total.setReadOnly(True)
        
        self.erros.setReadOnly(True)
        
      

    # Abre e fecha o Menu 
    def leftMenu(self):

        width = self.menu_bar.width()
        
        if width == 60:
            newWidth = 160
        else: 
            newWidth = 60

        self.animation = QtCore.QPropertyAnimation(self.menu_bar, b"minimumWidth")
        self.animation.setDuration(500)
        self.menu_bar.setFixedWidth(newWidth)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        window.setFixedHeight(window.height()) 
        
    def salvar(self):

        # # Valor que ela quer alterar 
        Caminho = self.caminho_excel.text() 
        
        Caminho = f"{Caminho}".replace('"', '')
        
        # tentar ler o arquivo excel, se não conseguir aparece a mensagem 
        try:
            excel = pd.read_excel(Caminho)
        except Exception as err:
            msg = QMessageBox()
            msg.setWindowTitle("Arcano </>")
            msg.setText(f"Erro ao ler a planilha excel, verifique o caminho")
            msg.setStyleSheet("QMessageBox {background-color: #F0F0F0;}")  # Defina o estilo do QMessageBox
            msg.exec()  
            return
            
        # Lista das colunas esperadas
        colunas_esperadas = ["Colunas esperada"]

        # Verificar se todas as colunas esperadas estão presentes no arquivo Excel
        colunas_presentes = excel.columns.tolist()
        for coluna in colunas_esperadas:
            if coluna not in colunas_presentes:
                msg = QMessageBox()
                msg.setWindowTitle("Arcano </>")
                msg.setText(f"A coluna '{coluna}' não foi encontrada no arquivo Excel.\nPor favor, verifique se as colunas têm o mesmo nome que o exemplo acima")
                msg.setStyleSheet("QMessageBox {background-color: #F0F0F0;}")  # Defina o estilo do QMessageBox
                msg.exec() 
                return 
        
        # CRIAR O CÓDIGO QUE DESEJA FAZER PARA A PLANILHA 

    def limpar(self):       
       self.erros.clear()  

    def consultar(self):
        
        empresa = self.filtro_Empresa.currentText() 
        numero = empresa.split("-")[0].strip().lstrip("0")
        numero_str = numero
        
        Unidade = self.filtro_unidade.currentText() 
        
        mes = self.filtro_mes.currentText() 
        
        Ano = self.filtro_ano.currentText() 
        
        #################################################################
        mes = '01' if mes == 'Janeiro' else mes
        mes = '02' if mes == 'Fevereiro' else mes
        mes = '03' if mes == 'Março' else mes
        mes = '04' if mes == 'Abril' else mes
        mes = '05' if mes == 'Maio' else mes
        mes = '06' if mes == 'Junho' else mes
        mes = '07' if mes == 'Julho' else mes
        mes = '08' if mes == 'Agosto' else mes
        mes = '09' if mes == 'Setembro' else mes
        mes = '10' if mes == 'Outubro' else mes
        mes = '11' if mes == 'Novembro' else mes
        mes = '12' if mes == 'Dezembro' else mes
        ##################################################################
        
        #Logica para trazer os campos que a pessoa seleciona como filtro para mostrar ao lado a tabela 
        if empresa not in "EMPRESA":
            
        
            if  Unidade == "UNIDADE" and mes == "MÊS" and Ano == "ANO": 
                
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1"
    
            elif Unidade == "UNIDADE" and mes != "MÊS" and  Ano == "ANO":
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND EXTRACT(MONTH FROM PERIODO) = :2"
                
          
            elif Unidade == "UNIDADE" and mes == "MÊS" and  Ano != "ANO":
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND EXTRACT(YEAR FROM PERIODO) = :2"

         
            elif Unidade == "UNIDADE" and mes != "MÊS" and  Ano != "ANO":  
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND EXTRACT(MONTH FROM PERIODO) = :2 AND EXTRACT(YEAR FROM PERIODO) = :3"
          
            elif  Unidade != "UNIDADE" and mes == "MÊS" and Ano == "ANO": 
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND FILIAL = :2"

            elif Unidade != "UNIDADE" and mes != "MÊS" and  Ano == "ANO":   
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND FILIAL = :2 AND EXTRACT(MONTH FROM PERIODO) = :3"
        
            elif Unidade != "UNIDADE" and mes == "MÊS" and  Ano != "ANO":             
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND FILIAL = :2 AND EXTRACT(YEAR FROM PERIODO) = :3"

            elif Unidade != "UNIDADE" and mes != "MÊS" and  Ano != "ANO":              
                total_1 = "SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE COD_FILIAL LIKE :1 AND FILIAL = :2 AND EXTRACT(MONTH FROM PERIODO) = :3 AND EXTRACT(YEAR FROM PERIODO) = :4"

        else:
            if  mes == "MÊS" and Ano == "ANO":          
                total_1 = f'SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA'
      
            elif mes != "MÊS" and  Ano == "ANO":
                total_1 = f'SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE EXTRACT(MONTH FROM PERIODO) = :1'

            elif mes == "MÊS" and  Ano != "ANO":
                total_1 = 'SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE EXTRACT(YEAR FROM PERIODO) = :1'       
         
   
            elif mes != "MÊS" and  Ano != "ANO":
                total_1 = 'SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA WHERE EXTRACT(YEAR FROM PERIODO) = :Ano AND EXTRACT(MONTH FROM PERIODO) = :mes_ciclo'


        model = QStandardItemModel()

        self.total.clear()
        
        model.removeRows(0, model.rowCount())
        soma = []

        model.setHorizontalHeaderLabels(["PERIODO", "COD_FILIAL", "FILIAL", "CATEGORIA", "PERFIL_CLIENTE", "METAS_VENDAS", "UF_FILIAL", "MARGEM"])

        row = 0
        for resultado in total_1:
            periodo = resultado[0]
            data_sem_hora = periodo.date()
            data_formatada = data_sem_hora.strftime('%d/%m/%Y')
            cod_filial = str(resultado[1]).zfill(8)
            filial = resultado[2]
            categoria = resultado[3]
            perfil_cliente = resultado[4]
            metas_vendas = resultado[5]
            soma.append(metas_vendas)
            meta_vendas = locale.format_string('%.2f', metas_vendas, grouping=True)
            uf_filial = resultado[6]
            margem = resultado[7]
            margem_porcentagem = margem * 100
            margem_real = (f"{margem_porcentagem:.0f}%")

            model.setItem(row, 0, QStandardItem(str(data_formatada)))
            model.setItem(row, 1, QStandardItem(str(cod_filial)))
            model.setItem(row, 2, QStandardItem(str(filial)))
            model.setItem(row, 3, QStandardItem(str(categoria)))
            model.setItem(row, 4, QStandardItem(str(perfil_cliente)))
            model.setItem(row, 5, QStandardItem(str(f"R$ {meta_vendas}")))
            model.setItem(row, 6, QStandardItem(str(uf_filial)))
            model.setItem(row, 7, QStandardItem(str(margem_real)))
            row += 1

        soma_total = sum(soma)
        soma_total_format = locale.format_string('%.2f', soma_total, grouping=True)

        self.total.setText(f"R$ {soma_total_format}")

        self.table_filtro.setModel(model)

        for row in range(model.rowCount()):
            self.table_filtro.setRowHeight(row, 1)

        self.table_filtro.verticalHeader().setVisible(False)
        font = QFont()
        font.setPointSize(10)
        self.table_filtro.setFont(font)
        self.table_filtro.setItemDelegate(QStyledItemDelegate())
        self.table_filtro.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_filtro.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        class AlternatingRowDelegate(QStyledItemDelegate):
            def initStyleOption(self, option, index):
                super().initStyleOption(option, index)
                if index.row() % 2 == 0:
                    option.backgroundBrush = Qt.lightGray

        delegate = AlternatingRowDelegate()
        for row in range(model.rowCount()):
            self.table_filtro.setItemDelegateForRow(row, delegate)

        self.table_filtro.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
    def gerar_excel(self):
        total_1 = f'SELECT PERIODO, COD_FILIAL, FILIAL, CATEGORIA, PERFIL_CLIENTE, METAS_VENDAS, UF_FILIAL, MARGEM FROM METAS_ESPECIALISTA'
    

        dados = []
        
        for excel in total_1:
            periodo = excel[0]
            cod_filial = excel[1]
            codigo = f"{cod_filial}".zfill(8)
            filial = excel[2]
            categoria = excel[3]
            perfil_cliente =excel[4]
            meta_vendas = excel[5]
            uf_filial = excel[6]
            margem = excel[7]
            margem_porcento = margem * 10 
            marge = "{:.2f}".format(margem_porcento)
            
            dados.append([periodo, codigo, filial, categoria, perfil_cliente, meta_vendas, uf_filial, marge])

        # Criando um DataFrame com os dados
        df = pd.DataFrame(dados, columns=["PERIODO", "COD_FILIAL", "FILIAL", "CATEGORIA", "PERFIL_CLIENTE", "METAS_VENDAS", "UF_FILIAL", "MARGEM"])

        # Exportando para um arquivo Excel temporário
        excel_file = "dados_consulta.xlsx"
        df.to_excel(excel_file, index=False)

        # Identificando o caminho da pasta de downloads
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # Exportando para um arquivo Excel na pasta de downloads
        excel_file = os.path.join(downloads_path, "dados_consulta.xlsx")
        df.to_excel(excel_file, index=False)
        
        msg = QMessageBox()
        msg.setWindowTitle("Arcano </>")
        msg.setText("Excel salvo na pasta de Downloads")
        msg.setIconPixmap(QIcon("caminho/para/seu/icone.png").pixmap(64, 64))  # Defina o caminho e o tamanho do ícone
        msg.setStyleSheet("QMessageBox {background-color: #F0F0F0;}")  # Defina o estilo do QMessageBox
        msg.exec()
        

            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    app.exec()