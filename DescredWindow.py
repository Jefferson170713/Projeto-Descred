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
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGroupBox
import os
import itertools
import numpy as np
import time
import locale
# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
from DescredJdbcPermission import JdbcPermissionDescred  

class DescredWindow:
    def __init__(self, parent=None):
        self.parent = parent
        self.file_path = None
        self.output_path = None
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
        
        
        # Botão para salvar
        btn_save = QPushButton("Processar e Salvar")
        btn_save.setFixedSize(150, 35)
        btn_save.clicked.connect(self.process_and_save)
        button_layout.addWidget(btn_save)
        
        main_layout.addLayout(button_layout)
        
        # Configurando o layout na aba
        descred_process.setLayout(main_layout)
    
    
    # Função para processar e salvar o arquivo
    def process_and_save(self):
        if ( self.df_search_descredenciado.empty) or ( self.df_search_substituto.empty ):
            QMessageBox.warning(self.parent, "Aviso", "Nenhum dado carregado para salvar!")
            return

        # Pede apenas o diretório onde salvar
        folder = QFileDialog.getExistingDirectory(
            self.parent,
            "Selecione a pasta para salvar o arquivo"
        )
        if not folder:
            return  # Usuário cancelou
        #  Add a função create_columns_key para criar as colunas de chave aqui
        self.create_columns_key()
        
        
        # Gera o nome do arquivo automaticamente
        cd_pessoa = str(self.df_search_descredenciado['CD_PESSOA'].iloc[0])
        date = self.pegar_data_atual()
        file_name = f"DESCREDENCIADO_{cd_pessoa}_{date}.csv"
        save_path = os.path.join(folder, file_name)

        try:
            #salvando no formato CSV em save_path
            self.df_search_descredenciado.to_csv(save_path, sep=';', encoding='latin1', index=False)
            # lançando uma mensagem de sucesso
            QMessageBox.information(self.parent, "Sucesso", f"Arquivo salvo com sucesso em:\n{save_path}")
        except Exception as erro:
            QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao salvar o arquivo:\n{str(erro)}")
    
    def pegar_data_atual(self):
        # Pega a data atual no formato dd_mm_yyyy
        return time.strftime("%d_%m_%Y")

    # Funções para limpar status específicos
    def clear_status_descredenciado(self):
        self.progress_bar_process_descredenciado.setValue(0)
        self.label_status_descredenciado.setText("Nenhum arquivo carregado - Descredenciado.")
        self.table_descredenciado.setRowCount(0)
        
    # Função para limpar o status de Substituto  
    def clear_status_substituto(self):
        self.progress_bar_process_substituto.setValue(0)
        self.label_status_substituto.setText("Nenhum arquivo carregado - Substituto.")
        self.table_substituto.setRowCount(0)
    
    # Funções de pesquisa
    def search_descredenciado(self):
        search_term = self.search_input_descredenciado.text()
        path_drive = r'./ARQUIVOS/Oracle_Jdbc/ojdbc8.jar'
        
        if search_term:
            try:
                dict_consulta = {}
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
                jdbc_permission = JdbcPermissionDescred(path_drive)
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

                dict_consulta = self.regime_exchange(dict_consulta)
                self.df_search_descredenciado['TIPO_CONSULTA'] = self.df_search_descredenciado.CONCAT_CONSULTA.map(dict_consulta)
                self.df_search_descredenciado['REDE_CONSULTA'] = self.df_search_descredenciado.CD_TIPO_REDE_ATENDIMENTO.astype(str) + '_' + self.df_search_descredenciado.TIPO_CONSULTA.astype(str)
                self.df_search_descredenciado['REDE_CONSULTA'] = self.df_search_descredenciado.apply(self.generate_query_network, axis=1)
                print(self.df_search_descredenciado.head())
                
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
                dict_consulta = {}
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
                    list_empresa.append('14')
                else:
                    list_empresa = ', '.join(map(str, list_empresa))
                
                if not list_empresa:
                    QMessageBox.warning(self.parent, "AVISO - SUBSTITUTO", "Por favor, selecione pelo menos uma operadora.\n\n - HAPVIDA\n - CCG\n - CLINIPAM\n - NDI MINAS\n - NDI SAÚDE")
                    return
                    
                # Instancia a classe JdbcPermission
                jdbc_permission = JdbcPermissionDescred(path_drive)
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
                
                dict_consulta = self.regime_exchange(dict_consulta)
                self.df_search_substituto['TIPO_CONSULTA'] = self.df_search_substituto.CONCAT_CONSULTA.map(dict_consulta)
                self.df_search_substituto['REDE_CONSULTA'] = self.df_search_substituto.CD_TIPO_REDE_ATENDIMENTO.astype(str) + '_' + self.df_search_substituto.TIPO_CONSULTA.astype(str)
                self.df_search_substituto['REDE_CONSULTA'] = self.df_search_substituto.apply(self.generate_query_network, axis=1)
                #print(self.df_search_substituto.head())

            except Exception as error:
                QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao buscar os dados: {str(error)}")
        else:
            QMessageBox.warning(self.parent, "AVISO - SUBSTITUTO", "Por favor, insira um termo de pesquisa válido.")
    
    def create_columns_key(self):
        # Criar a coluna KEY_PROCEDIMENTO_REDE para ambos os DataFrames
        self.df_search_descredenciado['KEY_PROCEDIMENTO_REDE'] = self.df_search_descredenciado['PROCEDIMENTO_TUSS'].astype(str) + '_' + self.df_search_descredenciado['CD_TIPO_REDE_ATENDIMENTO'].astype(str)
        self.df_search_substituto['KEY_PROCEDIMENTO_REDE'] = self.df_search_substituto['PROCEDIMENTO_TUSS'].astype(str) + '_' + self.df_search_substituto['CD_TIPO_REDE_ATENDIMENTO'].astype(str)
        # Criar um dicionário de mapeamento primeiro
        dict_rede_regime = self.df_search_substituto.set_index('KEY_PROCEDIMENTO_REDE')['REDE_CONSULTA'].to_dict()
        dict_regime = self.df_search_substituto.set_index('KEY_PROCEDIMENTO_REDE')['TIPO_CONSULTA'].to_dict()

        # Usar map() para fazer o mapeamento correto
        self.df_search_descredenciado['KEY_REDE_REGIME'] = self.df_search_descredenciado['KEY_PROCEDIMENTO_REDE'].map(dict_rede_regime).fillna('')
        self.df_search_descredenciado['KEY_TIPO_CONSULTA_SUBS'] = self.df_search_descredenciado['KEY_PROCEDIMENTO_REDE'].map(dict_regime).fillna('')
        
        # Aplicando a função para criar a coluna STATUS_REGIME
        self.df_search_descredenciado['STATUS_REGIME'] = self.df_search_descredenciado.apply(self.avaliar_status_regime, axis=1)
        # criando as colunas de status
        self.df_search_descredenciado['STATUS_KEY_PROCEDIMENTO_REDE'] = np.where(self.df_search_descredenciado['KEY_PROCEDIMENTO_REDE'].isin(self.df_search_substituto['KEY_PROCEDIMENTO_REDE']), 'SIM', 'NAO')
        self.df_search_descredenciado['STATUS_PROCEDIMENTO_TUSS'] = np.where(self.df_search_descredenciado['PROCEDIMENTO_TUSS'].isin(self.df_search_substituto['PROCEDIMENTO_TUSS']), 'SIM', 'NAO')
        self.df_search_descredenciado['STATUS_REDE'] = np.where(self.df_search_descredenciado['CD_TIPO_REDE_ATENDIMENTO'].isin(self.df_search_substituto['CD_TIPO_REDE_ATENDIMENTO']), 'SIM', 'NAO')
        # Aplicando a função
        self.df_search_descredenciado['ATENDIMENTO'] = self.criar_coluna_atendimento(
            self.df_search_descredenciado['TIPO_CONSULTA'], 
            self.df_search_descredenciado['KEY_TIPO_CONSULTA_SUBS']
        )
        
    def criar_coluna_atendimento(self, tipo_consulta_series, key_tipo_consulta_subs_series):
        # Convertendo para arrays numpy para melhor performance
        tipo_consulta = tipo_consulta_series.values
        key_tipo_consulta_subs = key_tipo_consulta_subs_series.values
        
        # Definindo as condições usando numpy
        conditions = [
            # T -> T = TOTAL
            (tipo_consulta == 'T') & (key_tipo_consulta_subs == 'T'),
            # T -> E = PARCIAL
            (tipo_consulta == 'T') & (key_tipo_consulta_subs == 'E'),
            # T -> U = PARCIAL
            (tipo_consulta == 'T') & (key_tipo_consulta_subs == 'U'),
            # E -> E = TOTAL
            (tipo_consulta == 'E') & (key_tipo_consulta_subs == 'E'),
            # E -> T = TOTAL
            (tipo_consulta == 'E') & (key_tipo_consulta_subs == 'T'),
            # E -> U = NAO
            (tipo_consulta == 'E') & (key_tipo_consulta_subs == 'U'),
            # U -> U = TOTAL
            (tipo_consulta == 'U') & (key_tipo_consulta_subs == 'U'),
            # U -> T = TOTAL
            (tipo_consulta == 'U') & (key_tipo_consulta_subs == 'T'),
            # U -> E = NAO
            (tipo_consulta == 'U') & (key_tipo_consulta_subs == 'E')
        ]
        # Definindo as escolhas correspondentes
        choices = [
            'TOTAL',    # T -> T
            'PARCIAL',  # T -> E
            'PARCIAL',  # T -> U
            'TOTAL',    # E -> E
            'TOTAL',    # E -> T
            'NAO',      # E -> U
            'TOTAL',    # U -> U
            'TOTAL',    # U -> T
            'NAO'       # U -> E
        ]
        # Usando numpy.select para aplicar as condições de forma vectorizada
        # default='NAO' para casos não cobertos (valores vazios, etc.)
        resultado = np.select(conditions, choices, default='NAO')
        
        # Convertendo de volta para série pandas
        return pd.Series(resultado, index=tipo_consulta_series.index)
    
    # Função para avaliar o STATUS_REGIME baseado nas regras definidas
    def avaliar_status_regime(self, row):
        tipo_consulta = row['TIPO_CONSULTA']
        tipo_consulta_subs = row['KEY_TIPO_CONSULTA_SUBS']
        rede_consulta = row['REDE_CONSULTA']
        key_rede_regime = row['KEY_REDE_REGIME']
        
        # Se não há correspondência na chave substituto, retorna NAO
        if pd.isna(tipo_consulta_subs) or tipo_consulta_subs == '':
            return 'NAO'
        
        # Situação 1: TIPO_CONSULTA = T (T tem precedência total)
        if tipo_consulta == 'T':
            # Se substituto também é T, verifica se são iguais
            if tipo_consulta_subs == 'T':
                return 'SIM' if rede_consulta == key_rede_regime else 'SIM'  # T->T sempre SIM
            # Se substituto é E ou U, verifica se KEY_REDE_REGIME está em REDE_CONSULTA
            elif tipo_consulta_subs in ['E', 'U']:
                # Como T gera múltiplas opções (T, E, U), verifica se a opção do substituto está presente
                return 'SIM' if key_rede_regime in rede_consulta else 'NAO'
            
        # Situação 2: TIPO_CONSULTA = E
        elif tipo_consulta == 'E':
            # Se substituto também é E, verifica se são iguais
            if tipo_consulta_subs == 'E':
                return 'SIM' if rede_consulta == key_rede_regime else 'SIM'  # E->E sempre SIM
            # Se substituto é T ou U, não há compatibilidade
            else:
                return 'NAO'
        
        # Situação 3: TIPO_CONSULTA = U
        elif tipo_consulta == 'U':
            # Se substituto também é U, verifica se são iguais
            if tipo_consulta_subs == 'U':
                return 'SIM' if rede_consulta == key_rede_regime else 'SIM'  # U->U sempre SIM
            # Se substituto é T ou E, não há compatibilidade
            else:
                return 'NAO'
        
        # Caso não se encaixe em nenhuma situação
        return 'NAO'
    
    def regime_exchange(self, dic_consulta):
       # Caracteres possíveis para cada posição
        opcoes_1 = ['T', '-']
        opcoes_2 = ['E', '-']
        opcoes_3 = ['U', '-']
        # Gerando todas as combinações de 6 posições
        combinacoes_1 = list(itertools.product(opcoes_1, repeat=6))
        combinacoes_2 = list(itertools.product(opcoes_2, repeat=6))
        combinacoes_3 = list(itertools.product(opcoes_3, repeat=6))
        # Criando o dicionário
        dic_consulta_1 = {
        '_'.join(comb): 'T' for comb in combinacoes_1
        }
        dic_consulta_2 = {
        '_'.join(comb): 'E' for comb in combinacoes_2
        }
        dic_consulta_3 = {
        '_'.join(comb): 'U' for comb in combinacoes_3
        }
        # excluiindo a combinação que tem todos os valores como '-'
        dic_consulta_1.pop('-_-_-_-_-_-', None)
        dic_consulta_2.pop('-_-_-_-_-_-', None)
        dic_consulta_3.pop('-_-_-_-_-_-', None)
        # criando um dicionário que junta os três dicionários 
        dic_consulta = {**dic_consulta_1, **dic_consulta_2, **dic_consulta_3}
        return dic_consulta
    
    def generate_query_network(self, row):
        rede = row['CD_TIPO_REDE_ATENDIMENTO']
        tipo = row['TIPO_CONSULTA']
        if tipo == 'T':
            # Retorna string com todas as opções separadas por vírgula
            return f'{rede}_T, {rede}_E, {rede}_U'
        else:
            return f'{rede}_{tipo}'
        
    def format_int(self, value):
        return locale.format_string('%.f', value, grouping=True)

