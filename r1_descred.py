import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout
import os


from PyQt5.QtWidgets import QWidget


# Classe principal da aplicação
class R1Descred(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HapDoc")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon(r'./Arquivos/logo/logo.ico'))
        self.r1_descred = QTabWidget()
        self.provider_descred = QWidget()
        # self.center_clinic = QWidget()
        # Instanciando a classe ProcedurePackageProcess
        self.procedure_package_process = QVBoxLayout()
        # self.center_clinic_process = WindowCenterClinic(parent=self)

        self.createview()

    # Função para criar as abas do programa
    def createview(self):
        space = 5 * ' '
        self.setCentralWidget(self.r1_descred)
        self.r1_descred.addTab(self.provider_descred, f'{space} Descredenciamento {space}')
        # self.r1_descred.addTab(self.center_clinic, f'{space} Centro Clínico {space}')
        self.r1_descred.setDocumentMode(True)
        self.r1_descred.setMovable(True)
        # Criando a aba "Pacote Procedimento"
        # self.procedure_package_process.create_procedures_and_package_tab(self.provider_descred)
        # self.center_clinic_process.create_center_clinic_tab(self.center_clinic)


# Loop do programa em funcionamento
def main():
    app = QApplication(sys.argv)
    window = R1Descred()
    window.show()
    sys.exit(app.exec_())

# Verifica se o arquivo é executado diretamente
if __name__ == "__main__":
    main()
        