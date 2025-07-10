import pandas as pd
import jaydebeapi
import time
import locale
from Arquivos.Oracle_jdbc.jdbc_permission import JdbcPermission

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class JdbcPermissionDescred:
    def __init__(self, driver_path):
        self.user = None
        self.password = None
        self.jdbc_driver = None
        self.jdbc_url = None
        self.query = None
        self.df = pd.DataFrame()
        self.progress_bar = None
        self.driver_path = driver_path
        
    def set_credentials(self):
        """
        Define as credenciais de acesso ao banco de dados.
        """
        credenciais = JdbcPermission()
        self.user, self.password, self.jdbc_driver, self.jdbc_url = credenciais.set_credentials()
        
        return self.user, self.password, self.jdbc_driver, self.jdbc_url
    
    def get_query(self, protocol=None, list_empresa=None):
        """
        Retorna a consulta SQL para buscar os dados de descredenciamento.
        """
        credenciais = JdbcPermission()
        self.query = credenciais.get_query_descred(protocol, list_empresa)
        
        return self.query
    
    def fetch_data(self, chunk_size=50000, protocol=None, progress_bar=None, list_empresa=None):
        
        # Configura as credenciais antes de conectar
        self.set_credentials()
        
        query = self.get_query(protocol, list_empresa)
        
        count_query = f"SELECT COUNT(*) FROM ({query})"

        try:
            conn = jaydebeapi.connect(
                self.jdbc_driver,
                self.jdbc_url,
                [self.user, self.password],
                self.driver_path
            )
            
            print("Conexão estabelecida com sucesso.")
            print(f'lista das empresas: {list_empresa}')

            # Conta as linhas
            cursor = conn.cursor()
            cursor.execute(count_query)
            qtd_linhas = cursor.fetchone()[0]
            qtd_solicitacoes = qtd_linhas // chunk_size + (1 if qtd_linhas % chunk_size > 0 else 0)
            qtd_linhas = self.format_int(qtd_linhas)
            print(f"Quantidade total de linhas: {qtd_linhas} Solicitações: {qtd_solicitacoes}")
            cursor.close()

            cursor = conn.cursor()
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]

            all_chunks = []
            total_linhas_baixadas = 0  # acumulador
            num = 0
            time_start = time.time()
            
            while True:
                rows = cursor.fetchmany(chunk_size)
                if not rows:
                    break
                df_chunk = pd.DataFrame(rows, columns=columns)
                all_chunks.append(df_chunk)
                qtd_linhas_df = len(df_chunk)
                total_linhas_baixadas += qtd_linhas_df  # soma ao total
                
                # Formata apenas para exibição
                qtd_linhas_df_formatado = self.format_int(qtd_linhas_df)
                total_linhas_baixadas_formatado = self.format_int(total_linhas_baixadas)
                
                num += 1
                elapsed_time_end = time.time() - time_start
                faltam = qtd_solicitacoes - num
                tempo_medio = elapsed_time_end / num
                progresso_num = 0  
                
                if progress_bar is not None:
                    progresso = int((num / qtd_solicitacoes) * 100)
                    progresso_num = progresso
                    progress_bar.setValue(progresso)
                else:
                    progresso_num = int((num / qtd_solicitacoes) * 100)
            
                print(f" Extração n°: {num} Falta : {faltam} - Chunk extraído: {qtd_linhas_df_formatado} - linhas (Total baixado: {total_linhas_baixadas_formatado}) - Tempo: {elapsed_time_end:.2f} segundos - Tempo médio: {tempo_medio:.2f} segundos por chunk - Progresso: {progresso_num}%")

            cursor.close()
            conn.close()
            print("Conexão encerrada com sucesso.")

            self.df = pd.concat(all_chunks, ignore_index=True) if all_chunks else pd.DataFrame(columns=columns)

            return self.df

        except Exception as erro:
            print(f"Erro ao buscar dados: {erro}")
            raise
    
    def format_int(self, value):
        return locale.format_string('%.f', value, grouping=True)
    
if __name__ == "__main__":
    
    # Essa parte do código é para teste e execução direta do script.
    # caminho para o driver JDBC
    driver_path = r'./Arquivos/Oracle_jdbc/ojdbc8.jar'
    
    # protocolo de consulta SQL
    protocolo = '468718538'
    
    # Instanciando a classe
    
    jdbc_permission = JdbcPermissionDescred(driver_path)
    
    # Marca o inicio do tempo
    start_time = time.time()
    
    # Busca dados
    df = jdbc_permission.fetch_data(chunk_size=50000, protocol=protocolo, list_empresa='1')
    
    # Marca o fim do tempo
    end_time = time.time()
    elapsed = end_time - start_time
    # Exibe os dados e o tempo
    print(f'Quantidade de linhas e colunas: {df.shape}')
    print(df)
    print(f"Tempo de execução: {elapsed:.2f} segundos")
    print(f"Tempo de execução: {elapsed / 60:.2f} minutos")
    
    
    