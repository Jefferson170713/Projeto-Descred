import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from DescredWindow import DescredWindow

from PyQt5.QtWidgets import QWidget

# Classe principal da aplicação
class R1Descred(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DESCRED")
        self.setGeometry(100, 100, 500, 600)
        self.setWindowIcon(QIcon(r'./Arquivos/logo/logo.ico'))
        self.r1_descred = QTabWidget()
        self.provider_descred = QWidget()
        self.procedure_descred = DescredWindow(parent=self)

        self.createview()

    # Função para criar as abas do programa
    def createview(self):
        space = 5 * ' '
        self.setCentralWidget(self.r1_descred)
        self.r1_descred.addTab(self.provider_descred, f'{space} Descredenciamento Total {space}')
        self.r1_descred.setDocumentMode(True)
        self.r1_descred.setMovable(True)
        self.procedure_descred.create_descred_window(self.provider_descred)

# Loop do programa em funcionamento
def main():
    app = QApplication(sys.argv)
    window = R1Descred()
    window.show()
    sys.exit(app.exec_())

# Verifica se o arquivo é executado diretamente
if __name__ == "__main__":
    main()
        