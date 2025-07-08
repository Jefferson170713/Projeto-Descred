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
import locale
# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
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
        btn_clear_status_desc.setFixedSize(100, 30)
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
        self.search_input_descredenciado.setFixedHeight(30)
        self.search_input_descredenciado.setPlaceholderText("Digite o(s) CD_PESSOA para o DESCREDENCIADO...")
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
        btn_clear_status_sub.setFixedSize(100, 30)
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
        self.search_input_substituto.setFixedHeight(30)
        self.search_input_substituto.setPlaceholderText("Digite o(s) CD_PESSOA para o SUBSTITUTO...")
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
        # btn_process = QPushButton("Processar")
        # btn_process.setFixedSize(150, 35)
        # btn_process.clicked.connect(self.process_data)
        # button_layout.addWidget(btn_process)
        
        # Adiciona um espaço expansível entre os botões
        #button_layout.addStretch()
        
        # Botão para salvar
        btn_save = QPushButton("Salvar")
        btn_save.setFixedSize(150, 35)
        btn_save.clicked.connect(self.process_and_save)
        button_layout.addWidget(btn_save)
        
        main_layout.addLayout(button_layout)
        
        # Configurando o layout na aba
        descred_process.setLayout(main_layout)
    
    
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
    

    # Funções para limpar status específicos
    def clear_status_descredenciado(self):
        # função para limpar o status de Descredenciado
        self.progress_bar_process_descredenciado.setValue(0)
        self.label_status_descredenciado.setText("Nenhum arquivo carregado - Descredenciado.")
        # limpando a tabela e deixando completamente em branco novamente
        self.table_descredenciado.setRowCount(0)
        
    # Função para limpar o status de Substituto  
    def clear_status_substituto(self):
        # função para limpar o status de Substituto
        self.progress_bar_process_substituto.setValue(0)
        self.label_status_substituto.setText("Nenhum arquivo carregado - Substituto.")
        # limpando a tabela e deixando completamente em branco novamente
        self.table_substituto.setRowCount(0)
    
    # Funções de pesquisa
    def search_descredenciado(self):
        search_term = self.search_input_descredenciado.text()
        path_drive = r'./ARQUIVOS/Oracle_Jdbc/ojdbc8.jar'
        
        if search_term:
            try:
                list_empresa = []
                if self.checkbox_desc_1.isChecked():
                    list_empresa.append('1')
                if self.checkbox_desc_2.isChecked():
                    list_empresa.append('8')
                if self.checkbox_desc_3.isChecked():
                    list_empresa.append('9')
                if self.checkbox_desc_4.isChecked():
                    list_empresa.append('10')
                if self.checkbox_desc_5.isChecked():
                    list_empresa.append('14')
                else:
                    list_empresa = ', '.join(map(str, list_empresa))
                
                if not list_empresa:
                    QMessageBox.warning(self.parent, "AVISO - DESCREDENCIADO", "Por favor, selecione pelo menos uma operadora.\n\n - HAPVIDA\n - CCG\n - CLINIPAM\n - NDI MINAS\n - NDI SAÚDE")
                    return
                    
                # Instancia a classe JdbcPermission
                jdbc_permission = JdbcPermission_descred(path_drive)
                # Usa o método fetch_data para buscar os dados
                self.df_search_descredenciado = jdbc_permission.fetch_data(chunk_size=50000, protocol=search_term, progress_bar=self.progress_bar_process_descredenciado, list_empresa=list_empresa)
                self.df_search_descredenciado = self.initial_treatment(self.df_search_descredenciado)
                number_of_lines = self.format_int(len(self.df_search_descredenciado))
                self.label_status_descredenciado.setText(f"{number_of_lines} linhas carregadas - Descredenciado.")
                
                # Atualiza a tabela com os dados encontrados
                self.table_descredenciado.setRowCount(len(self.df_search_descredenciado))
                self.table_descredenciado.setColumnCount(len(self.df_search_descredenciado.columns))
                self.table_descredenciado.setHorizontalHeaderLabels(self.df_search_descredenciado.columns)

                for row_idx, row_data in self.df_search_descredenciado.iterrows():
                    for col_idx, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))
                        self.table_descredenciado.setItem(row_idx, col_idx, item)

            except Exception as error:
                QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao buscar os dados: {str(error)}")
        else:
            QMessageBox.warning(self.parent, "AVISO - DESCREDENCIADO", "Por favor, insira um termo de pesquisa válido.")
            
    def initial_treatment(self, df):
        # Tratamento inicial dos dados
        df.CD_TIPO_REDE_ATENDIMENTO = df.CD_TIPO_REDE_ATENDIMENTO.fillna('-').astype(str).replace('.0', '')
        df.CD_PROCEDIMENTO = df.CD_PROCEDIMENTO.fillna('-').astype(str).replace('.0', '')
        df.PROCEDIMENTO_TUSS = df.PROCEDIMENTO_TUSS.fillna('-').astype(str).str.replace('.0', '')
        df.FL_CONSULTA = df.FL_CONSULTA.fillna('-').astype(str).replace('.0', '')
        df.FL_EXAME = df.FL_EXAME.fillna('-').astype(str).replace('.0', '')
        df.FL_TRATAMENTO = df.FL_TRATAMENTO.fillna('-').astype(str).replace('.0', '')
        df.FL_PQA = df.FL_PQA.fillna('-').astype(str).replace('.0', '')
        df.FL_INTERNACAO = df.FL_INTERNACAO.fillna('-').astype(str).replace('.0', '')
        df.FL_SERVICO = df.FL_SERVICO.fillna('-').astype(str).replace('.0', '')
        df.FL_PE = df.FL_PE.fillna('-').astype(str).replace('.0', '')
        # Criando a coluna de Key_consulta
        df['CONCAT_CONSULTA'] = df.FL_CONSULTA.astype(str) + '_' + df.FL_EXAME.astype(str) + '_' + df.FL_TRATAMENTO.astype(str) + '_' + df.FL_PQA.astype(str) + '_' + df.FL_INTERNACAO.astype(str) + '_' + df.FL_SERVICO.astype(str)
        return df
    
    def search_substituto(self):
        search_term = self.search_input_substituto.text()
        path_drive = r'./ARQUIVOS/Oracle_Jdbc/ojdbc8.jar'
        
        if search_term:
            try:
                list_empresa = []
                if self.checkbox_sub_1.isChecked():
                    list_empresa.append('1')
                if self.checkbox_sub_2.isChecked():
                    list_empresa.append('8')
                if self.checkbox_sub_3.isChecked():
                    list_empresa.append('9')
                if self.checkbox_sub_4.isChecked():
                    list_empresa.append('10')
                if self.checkbox_sub_5.isChecked():
                    list_empresa.append('10')
                else:
                    list_empresa = ', '.join(map(str, list_empresa))
                
                if not list_empresa:
                    QMessageBox.warning(self.parent, "AVISO - SUBSTITUTO", "Por favor, selecione pelo menos uma operadora.\n\n - HAPVIDA\n - CCG\n - CLINIPAM\n - NDI MINAS\n - NDI SAÚDE")
                    return
                    
                # Instancia a classe JdbcPermission
                jdbc_permission = JdbcPermission_descred(path_drive)
                # Usa o método fetch_data para buscar os dados
                self.df_search_substituto = jdbc_permission.fetch_data(chunk_size=50000, protocol=search_term, progress_bar=self.progress_bar_process_substituto, list_empresa=list_empresa)
                self.df_search_substituto = self.initial_treatment(self.df_search_substituto)
                number_of_lines = self.format_int(len(self.df_search_substituto))
                self.label_status_substituto.setText(f"{number_of_lines} linhas carregadas - Substituto.")
                
                # Atualiza a tabela com os dados encontrados
                self.table_substituto.setRowCount(len(self.df_search_substituto))
                self.table_substituto.setColumnCount(len(self.df_search_substituto.columns))
                self.table_substituto.setHorizontalHeaderLabels(self.df_search_substituto.columns)

                for row_idx, row_data in self.df_search_substituto.iterrows():
                    for col_idx, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))
                        self.table_substituto.setItem(row_idx, col_idx, item)

            except Exception as error:
                QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao buscar os dados: {str(error)}")
        else:
            QMessageBox.warning(self.parent, "AVISO - SUBSTITUTO", "Por favor, insira um termo de pesquisa válido.")
    
    # Função para processar dados
    def process_data(self):
        # Você implementará esta função
        pass
    
    
    def save_to_excel(self, df, file_path):
        ...
        
    def format_int(self, value):
        return locale.format_string('%.f', value, grouping=True)

