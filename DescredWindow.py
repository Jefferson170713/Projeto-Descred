import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGroupBox
import os
#from SearchWindow import SearchWindow
#from ARQUIVOS.Oracle_Jdbc.jdbc_teste_02 import JdbcPermission 
from Arquivos.Oracle_jdbc.script_jdbc_descred import JdbcPermission_descred

class DescredWindow:
    def __init__(self, parent=None):
        self.parent = parent
        self.file_path = None
        self.output_path = None
        self.df_descredenciado = pd.DataFrame()
        self.df_substituto = pd.DataFrame()
        self.progress_bar_process_descredenciado = None
        self.progress_bar_process_substituto = None
        self.df_search = pd.DataFrame()  # DataFrame para armazenar os dados pesquisados
        self.df_search_descredenciado = pd.DataFrame()  # DataFrame para Descredenciado
        self.df_search_substituto = pd.DataFrame()  # DataFrame para Substituto
        
        # Checkboxes para Descredenciado
        self.checkbox_desc_1 = None
        self.checkbox_desc_2 = None
        self.checkbox_desc_3 = None
        self.checkbox_desc_4 = None
        self.checkbox_desc_5 = None
        
        # Checkboxes para Substituto
        self.checkbox_sub_1 = None
        self.checkbox_sub_2 = None
        self.checkbox_sub_3 = None
        self.checkbox_sub_4 = None
        self.checkbox_sub_5 = None
        
        # Campos de pesquisa
        self.search_input_descredenciado = None
        self.search_input_substituto = None
        
        # Tabelas
        self.table_descredenciado = None
        self.table_substituto = None

    def create_descred_window(self, descred_process):
        # Layout principal
        main_layout = QVBoxLayout()
        
        # ========== SEÇÃO DESCREDENCIADO ==========
        # Grupo para Descredenciado
        group_descredenciado = QGroupBox("DESCREDENCIADO")
        layout_descredenciado = QVBoxLayout()
        
        # Status layout para Descredenciado
        status_layout_desc = QHBoxLayout()
        self.label_status_descredenciado = QLabel("Nenhum arquivo carregado - Descredenciado.")
        status_layout_desc.addWidget(self.label_status_descredenciado)
        status_layout_desc.addStretch()
        
        btn_clear_status_desc = QPushButton("Limpar Status")
        btn_clear_status_desc.setFixedSize(100, 35)
        btn_clear_status_desc.clicked.connect(self.clear_status_descredenciado)
        status_layout_desc.addWidget(btn_clear_status_desc)
        layout_descredenciado.addLayout(status_layout_desc)
        
        # Barra de progresso para Descredenciado
        self.progress_bar_process_descredenciado = QProgressBar()
        self.progress_bar_process_descredenciado.setValue(0)
        self.progress_bar_process_descredenciado.setMinimum(0)
        self.progress_bar_process_descredenciado.setMaximum(100)
        layout_descredenciado.addWidget(self.progress_bar_process_descredenciado)
        
        # 5 Checkboxes para Descredenciado
        checkboxes_layout_desc = QHBoxLayout()
        self.checkbox_desc_1 = QCheckBox("HAPVIDA")
        self.checkbox_desc_2 = QCheckBox("CCG")
        self.checkbox_desc_3 = QCheckBox("CLINIPAM")
        self.checkbox_desc_4 = QCheckBox("NDI MINAS")
        self.checkbox_desc_5 = QCheckBox("NDI SAÚDE")
        
        checkboxes_layout_desc.addWidget(self.checkbox_desc_1)
        checkboxes_layout_desc.addWidget(self.checkbox_desc_2)
        checkboxes_layout_desc.addWidget(self.checkbox_desc_3)
        checkboxes_layout_desc.addWidget(self.checkbox_desc_4)
        checkboxes_layout_desc.addWidget(self.checkbox_desc_5)
        layout_descredenciado.addLayout(checkboxes_layout_desc)
        
        # Campo de pesquisa e botão para Descredenciado
        search_layout_desc = QHBoxLayout()
        self.search_input_descredenciado = QLineEdit()
        self.search_input_descredenciado.setPlaceholderText("Digite os protocolos para Descredenciado...")
        search_layout_desc.addWidget(self.search_input_descredenciado)
        
        btn_search_desc = QPushButton("Buscar")
        btn_search_desc.setFixedSize(100, 30)
        btn_search_desc.clicked.connect(self.search_descredenciado)
        search_layout_desc.addWidget(btn_search_desc)
        layout_descredenciado.addLayout(search_layout_desc)
        
        # Tabela para Descredenciado
        self.table_descredenciado = QTableWidget()
        self.table_descredenciado.setMaximumHeight(150)  # Mostra aproximadamente 5 linhas
        layout_descredenciado.addWidget(self.table_descredenciado)
        
        group_descredenciado.setLayout(layout_descredenciado)
        main_layout.addWidget(group_descredenciado)
        
        # ========== SEPARADOR ==========
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)
        
        # ========== SEÇÃO SUBSTITUTO ==========
        # Grupo para Substituto
        group_substituto = QGroupBox("SUBSTITUTO")
        layout_substituto = QVBoxLayout()
        
        # Status layout para Substituto
        status_layout_sub = QHBoxLayout()
        self.label_status_substituto = QLabel("Nenhum arquivo carregado - Substituto.")
        status_layout_sub.addWidget(self.label_status_substituto)
        status_layout_sub.addStretch()
        
        btn_clear_status_sub = QPushButton("Limpar Status")
        btn_clear_status_sub.setFixedSize(100, 35)
        btn_clear_status_sub.clicked.connect(self.clear_status_substituto)
        status_layout_sub.addWidget(btn_clear_status_sub)
        layout_substituto.addLayout(status_layout_sub)
        
        # Barra de progresso para Substituto
        self.progress_bar_process_substituto = QProgressBar()
        self.progress_bar_process_substituto.setValue(0)
        self.progress_bar_process_substituto.setMinimum(0)
        self.progress_bar_process_substituto.setMaximum(100)
        layout_substituto.addWidget(self.progress_bar_process_substituto)
        
        # 5 Checkboxes para Substituto
        checkboxes_layout_sub = QHBoxLayout()
        self.checkbox_sub_1 = QCheckBox("HAPVIDA")
        self.checkbox_sub_2 = QCheckBox("CCG")
        self.checkbox_sub_3 = QCheckBox("CLINIPAM")
        self.checkbox_sub_4 = QCheckBox("NDI MINAS")
        self.checkbox_sub_5 = QCheckBox("NDI SAÚDE")
        
        checkboxes_layout_sub.addWidget(self.checkbox_sub_1)
        checkboxes_layout_sub.addWidget(self.checkbox_sub_2)
        checkboxes_layout_sub.addWidget(self.checkbox_sub_3)
        checkboxes_layout_sub.addWidget(self.checkbox_sub_4)
        checkboxes_layout_sub.addWidget(self.checkbox_sub_5)
        layout_substituto.addLayout(checkboxes_layout_sub)
        
        # Campo de pesquisa e botão para Substituto
        search_layout_sub = QHBoxLayout()
        self.search_input_substituto = QLineEdit()
        self.search_input_substituto.setPlaceholderText("Digite os protocolos para Substituto...")
        search_layout_sub.addWidget(self.search_input_substituto)
        
        btn_search_sub = QPushButton("Buscar")
        btn_search_sub.setFixedSize(100, 30)
        btn_search_sub.clicked.connect(self.search_substituto)
        search_layout_sub.addWidget(btn_search_sub)
        layout_substituto.addLayout(search_layout_sub)
        
        # Tabela para Substituto
        self.table_substituto = QTableWidget()
        self.table_substituto.setMaximumHeight(150)  # Mostra aproximadamente 5 linhas
        layout_substituto.addWidget(self.table_substituto)
        
        group_substituto.setLayout(layout_substituto)
        main_layout.addWidget(group_substituto)
        
        # ========== BOTÕES FINAIS ==========
        # Layout horizontal para os botões finais
        button_layout = QHBoxLayout()
        
        # Botão para processar dados
        btn_process = QPushButton("Processar")
        btn_process.setFixedSize(150, 35)
        btn_process.clicked.connect(self.process_data)
        button_layout.addWidget(btn_process)
        
        # Adiciona um espaço expansível entre os botões
        button_layout.addStretch()
        
        # Botão para salvar
        btn_save = QPushButton("Salvar")
        btn_save.setFixedSize(150, 35)
        btn_save.clicked.connect(self.process_and_save)
        button_layout.addWidget(btn_save)
        
        main_layout.addLayout(button_layout)
        
        # Configurando o layout na aba
        descred_process.setLayout(main_layout)
    
    # Função para pesquisar no banco por protocolo
    def searchwindow(self):
        # Cria uma instância da janela de pesquisa
        search_window = SearchWindow(self.parent)
        search_window.exec_()  # Exibe a janela de forma modal
        self.df_search = search_window.df_search
    
    # Função para processar e salvar o arquivo
    def process_and_save(self):
        if self.df_search.empty:
            QMessageBox.warning(self.parent, "Aviso", "Nenhum dado carregado para salvar!")
            return

        # Pede apenas o diretório onde salvar
        folder = QFileDialog.getExistingDirectory(
            self.parent,
            "Selecione a pasta para salvar o arquivo"
        )
        if not folder:
            return  # Usuário cancelou

        # Gera o nome do arquivo automaticamente
        protocolo = str(self.df_search['CD_PROTOCOLO'].iloc[0])
        file_name = f"PROTOCOLO_{protocolo}.xlsx"
        save_path = os.path.join(folder, file_name)

        try:
            # self.df_search = self.adjust_values()
            # self.progress_bar_process.setValue(20)
            # self.df_search = self.creating_the_master_key()
            # self.progress_bar_process.setValue(45)
            # self.df_search = self.grouping_the_networks()
            # self.progress_bar_process.setValue(75)
            # self.df_search = self.breaking_the_primary_key_into_columns()
            # self.progress_bar_process.setValue(95)

            # self.save_to_excel(self.df_search, save_path)

            self.progress_bar_process.setValue(100)
            self.label_status_win_one.setText(f"{self.df_search.shape[0]} linhas carregadas e salvas no arquivo Excel.")
            #QMessageBox.information(self.parent, "Sucesso", f"Arquivo salvo em:\n{save_path}")
        except Exception as erro:
            QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao salvar o arquivo:\n{str(erro)}")
    
    # Função para limpar o status
    def clear_status(self):
        # self.progress_bar_process.setValue(0)
        # self.label_status_win_one.setText("Nenhum arquivo carregado.")
        ...
    
    # Funções para limpar status específicos
    def clear_status_descredenciado(self):
        # Você implementará esta função
        pass
        
    def clear_status_substituto(self):
        # Você implementará esta função
        pass
    
    # Funções de pesquisa
    def search_descredenciado(self):
        # Você implementará esta função
        self.searchwindow()
    
    def search_substituto(self):
        # Você implementará esta função
        pass
    
    # Função para processar dados
    def process_data(self):
        # Você implementará esta função
        pass
    
    
    
    def save_to_excel(self, df, file_path):
        ...



class SearchWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pesquisar Dados")
        self.setFixedSize(600, 400)  # Tamanho fixo da janela
        self.init_ui()
        self.df_search = pd.DataFrame()  # DataFrame para armazenar os dados pesquisados
        self.parent = parent  # Armazena a referência ao widget pai
        #elf.progress_bar_process_search = None

    def init_ui(self):
        # Cria o layout principal
        main_layout = QVBoxLayout()

        # Linha para entrada de texto e botão de pesquisa
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Digite os Protocolos...")
        search_layout.addWidget(self.search_input)

        btn_search = QPushButton("Pesquisar")
        btn_search.setFixedSize(100, 30)
        btn_search.clicked.connect(self.perform_search)  # Conecta à função de pesquisa
        search_layout.addWidget(btn_search)

        # Barra de progresso (agora como atributo da classe)
        self.progress_bar_process_search = QProgressBar()
        self.progress_bar_process_search.setValue(0)
        self.progress_bar_process_search.setMinimum(0)
        self.progress_bar_process_search.setMaximum(100)
        main_layout.addWidget(self.progress_bar_process_search)

        self.label_status = QLabel("Status: Nenhuma pesquisa realizada.")
        main_layout.addWidget(self.label_status)


        main_layout.addLayout(search_layout)

        # Separador
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator1)

        # Tabela para exibir os resultados
        self.table = QTableWidget()
        self.table.setColumnCount(19)  # Define 19 colunas
        self.table.setHorizontalHeaderLabels(
            ['CD_PESSOA', 'NU_CGC_CPF', 'CD_PROCEDIMENTO', 'PROCEDIMENTO_TUSS',
            'CD_TIPO_REDE_ATENDIMENTO', 'FL_DISPONIVEL_LIVRO', 'FL_DISPONIVEL_WEB',
            'DT_INICIO_VIGENCIA', 'DT_FIM_VIGENCIA', 'FL_CONSULTA', 'FL_EXAME',
            'FL_TRATAMENTO', 'FL_PQA', 'FL_INTERNACAO', 'FL_SERVICO',
            'VL_ORDEM_PRIORIDADE', 'FL_PE', 'CD_EMPRESA_PLANO', 'TIPO_TELA']
        )
        main_layout.addWidget(self.table)

        # Separador
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator2)

        # Botão para armazenar a informação (centralizado)
        btn_store_layout = QHBoxLayout()
        btn_store = QPushButton("Armazenar Informação")
        btn_store.setFixedSize(200, 40)
        btn_store.clicked.connect(self.store_information)  # Conecta à função de armazenamento
        btn_store_layout.addStretch()  # Adiciona espaço antes do botão
        btn_store_layout.addWidget(btn_store)
        btn_store_layout.addStretch()  # Adiciona espaço depois do botão
        main_layout.addLayout(btn_store_layout)

        # Adiciona o layout principal a um widget para o QScrollArea
        container_widget = QWidget()
        container_widget.setLayout(main_layout)

        # Cria uma área de rolagem
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(container_widget)

        # Define o layout da janela
        window_layout = QVBoxLayout()
        window_layout.addWidget(scroll_area)
        self.setLayout(window_layout)

    def perform_search(self):
        # Obtém o termo de pesquisa e o caminho do driver JDBC
        search_term = self.search_input.text()
        path_drive = r'./ARQUIVOS/Oracle_Jdbc/ojdbc8.jar'

        if search_term:
            try:
                # Instancia a classe JdbcPermission
                jdbc_permission = JdbcPermission_descred(path_drive)
                #jdbc_permission = None

                # Usa o método fetch_data para buscar os dados
                #self.df_search, protocol = jdbc_permission.fetch_data(protocol=search_term, chunk_size=50000, progress_bar=self.progress_bar_process_search)
                self.df_search = jdbc_permission.fetch_data(chunk_size=50000, protocol=search_term)
                protocol = search_term

                self.label_status.setText(f"{len(self.df_search)} linhas carregadas.")
                # Atualiza o self.df_search com os dados encontrados
                #self.df_search = df

                # Define o número de linhas e colunas da tabela com base no DataFrame
                self.table.setRowCount(len(self.df_search))
                self.table.setColumnCount(len(self.df_search.columns))
                self.table.setHorizontalHeaderLabels(self.df_search.columns)

                # Preenche a tabela com os dados do DataFrame
                for row_idx, row_data in self.df_search.iterrows():
                    for col_idx, cell_data in enumerate(row_data):
                        self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

                if self.df_search.empty:
                    QMessageBox.warning(self, 'Aviso', f'Protocolo(s): ( {protocol} ) inelegível para automatização de documentos. \n\nSolicita-se verificação com a coordenação.')

            except Exception as erro:
                QMessageBox.critical(self, "Erro", f"Erro ao buscar dados:\n{str(erro)}")
        else:
            QMessageBox.warning(self, "Aviso", "Digite um termo para pesquisar!")

    def store_information(self):
        # Verifica se há dados no DataFrame
        if self.df_search.empty:
            QMessageBox.warning(self, "Aviso", "Nenhuma informação foi encontrada para armazenar!")
            return None

        # Exibe uma mensagem de sucesso e retorna o DataFrame
        QMessageBox.information(self, "Informação", "Informação armazenada com sucesso!")
        return self.df_search