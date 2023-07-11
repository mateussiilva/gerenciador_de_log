from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de exibição de linhas de arquivo")
        self.setGeometry(100, 100, 500, 300)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.load_file_content()

    def load_file_content(self):
        file_path = 'tex_log_limpo.txt'  # Substitua pelo caminho correto do arquivo
        with open(file_path, 'r') as file:
            content = file.read()
            self.text_edit.setPlainText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
