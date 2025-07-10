# 🏥 Descred - Sistema de Automação para Descredenciamento de Prestadores

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://pypi.org/project/PyQt5/)
[![Oracle](https://img.shields.io/badge/Database-Oracle-red.svg)](https://www.oracle.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-yellow.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

## 📋 Sobre o Projeto

O **Descred** é um sistema de automação inteligente desenvolvido para otimizar o processo de descredenciamento de prestadores de serviços médicos. O programa automatiza a análise de compatibilidade entre prestadores descredenciados e seus substitutos, determinando se o prestador substituto pode absorver todos os serviços oferecidos.

### 🎯 Problema Resolvido

Anteriormente, o processo de descredenciamento era realizado manualmente:
- ⏱️ **30+ minutos** para extrair dados de um prestador com 500.000 registros
- 🔄 **Processo duplicado** (descredenciado + substituto)
- ❌ **Propenso a erros** humanos durante manipulação de grandes volumes
- 📊 **Análise manual** de compatibilidade entre prestadores

### 💡 Solução Implementada

- ⚡ **3,5 minutos** para extrair 500.000 registros (melhoria de ~90%)
- 🤖 **Automação completa** do processo de análise
- ✅ **Zero erros** de processamento
- 📈 **Análise inteligente** de compatibilidade

## 🚀 Funcionalidades Principais

### 🔍 **Busca Otimizada**
- Conexão direta com banco de dados Oracle
- Extração em chunks de 50.000 registros
- Barra de progresso em tempo real
- Tratamento de grandes volumes de dados

### 📊 **Análise Inteligente**
- **Compatibilidade de Procedimentos**: Verifica se o substituto oferece os mesmos procedimentos TUSS
- **Análise de Rede**: Valida se atende nas mesmas redes da operadora
- **Classificação de Atendimento**: 
  - `TOTAL` - Substituto cobre completamente
  - `PARCIAL` - Substituto cobre parcialmente  
  - `NAO` - Substituto não cobre
- **Status de Regime**: Análise baseada em regras de precedência (T → E → U)

### 📁 **Exportação Automatizada**
- Geração de relatórios em CSV
- Nomenclatura automática com timestamp
- Encoding otimizado para sistemas brasileiros

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **PyQt5** - Interface gráfica moderna
- **Pandas** - Manipulação e análise de dados
- **Oracle Database** - Conexão via JDBC
- **JayDeBeApi** - Driver JDBC para Python
- **NumPy** - Operações numéricas otimizadas

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Oracle JDBC Driver (ojdbc8.jar)
- Acesso ao banco de dados Oracle da empresa

## 🔧 Instalação

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/descred.git
cd descred
```

### 2. Criação do Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Atualizar o pip
```bash
python -m pip install --upgrade pip
```

### 4. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 5. Configuração do Driver Oracle
- Certifique-se de que o arquivo `ojdbc8.jar` está na pasta `Arquivos/Oracle_jdbc/`
- Configure as credenciais de acesso no arquivo apropriado

## 🚀 Como Usar

### 1. Iniciar a Aplicação
```bash
python Descred.py
```

### 2. Processo de Descredenciamento

#### **Passo 1: Prestador Descredenciado**
1. Selecione a(s) operadora(s)
2. Digite o CD_PESSOA do prestador
3. Clique em "Buscar"
4. Aguarde o carregamento dos dados

#### **Passo 2: Prestador Substituto**
1. Selecione a(s) operadora(s)
2. Digite o CD_PESSOA do substituto
3. Clique em "Buscar"
4. Aguarde o carregamento dos dados

#### **Passo 3: Processamento**
1. Clique em "Processar e Salvar"
2. Selecione o diretório de destino
3. Aguarde a geração do relatório

### 3. Saída do Programa
O sistema gera um arquivo CSV com:
- Dados originais do prestador descredenciado
- Colunas de análise de compatibilidade
- Status de regime e atendimento
- Classificação final da substituição

## 📊 Estrutura do Projeto

```
Descred/
├── Descred.py                 # Arquivo principal da aplicação
├── DescredWindow.py           # Interface gráfica (PyQt5)
├── DescredJdbcPermission.py   # Conexão e extração de dados
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação
├── LICENSE                    # Licença MIT
└── Arquivos/
    ├── logo/                  # Logos da aplicação
    └── Oracle_jdbc/           # Drivers e configurações Oracle
        ├── ojdbc8.jar
        └── jdbc_permission.py
```

## 📈 Performance

### Benchmarks de Extração
| Volume de Dados | Método Manual | Descred | Melhoria |
|-----------------|---------------|---------|----------|
| 100.000 registros | ~6 min | ~42 seg | 88% |
| 500.000 registros | ~30 min | ~3.5 min | 88% |
| 1.000.000 registros | ~60 min | ~7 min | 88% |

### Recursos Otimizados
- ⚡ Extração em chunks para otimização de memória
- 🔄 Processamento vetorizado com NumPy
- 📊 Interface responsiva com feedback em tempo real
- 🛡️ Tratamento robusto de erros

## 👥 Público-Alvo

Este sistema foi desenvolvido especificamente para as **equipes R1 e R2** do setor de análise de prestadores, proporcionando:

- **Analistas de Dados**: Automação completa do processo de análise
- **Gestores de Operações**: Relatórios padronizados e confiáveis  
- **Equipe Técnica**: Redução significativa do tempo operacional

## 🤝 Contribuições

Este projeto foi desenvolvido com a colaboração especial da **Equipe R1**, através de múltiplas reuniões para compreensão detalhada dos processos de análise e requisitos específicos do negócio.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Jefferson** - Desenvolvedor Python | Especialista em Automação de Processos

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=Github&logoColor=white)](https://github.com/seu-usuario)

---

<p align="center">
  Desenvolvido com ❤️ para otimização de processos de saúde
</p>
