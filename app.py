import sys
# from PyQt6.QtCore import QtCore
# from PyQt6.QtGui import QtGui
from PyQt6.QtWidgets import QLabel,QPushButton,QApplication,QMainWindow
 
# vamos criar uma classe que herda de QMainWindow
class JanelaPrincipal(QMainWindow):
  # construtor da classe
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Sistema de LOG")
    self.setGeometry(0,0,600,500)
     
    # vamos criar um botão QPushButton
 
    # definimos este botão como o controle central
    # da janela principal
    # self.setCentralWidget(botao)
 
if __name__== "__main__":
  # cria a aplicação
  app = QApplication(sys.argv)
 
  # cria a janela principal e a coloca visível
  janela_principal = JanelaPrincipal()
  janela_principal.show()
 
  # executa a aplicação
  app.exec()