<h1 align="center">
  <img alt="Ícone Python" title="Ícone Python" src="https://github.com/pedromiguelsbs/weather-airflow/blob/main/assets/python-logo.png" width="120px" /> 
</h1> 

<h2 align="center">Pipeline ETL: Utilizando a API do GitHub + biblioteca Requests</h2> 

<p align="center">
 <a href="https://www.linkedin.com/in/pedromiguelsbs/">
   <img alt="Criado por" src="https://img.shields.io/static/v1?label=Criador&message=pedromiguelsbs&color=FFD34B&labelColor=000000">
 </a>
 <a href="https://github.com/pedromiguelsbs/repositories-requests/blob/main/LICENSE">
   <img alt="License" src="https://img.shields.io/static/v1?label=License&message=MIT&color=FFD34B&labelColor=000000">
 </a>
</p> 

<p align="center">
  <a href="#sobre">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#conteúdo">Conteúdo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#como-usar-este-repositório">Como utilizar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contribuições">Contribuições</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>

# Sobre 
Este repositório contém um projeto prático de ETL desenvolvido em Python que utiliza a biblioteca requests para se conectar à API do GitHub. O objetivo principal é extrair as linguagens de programação utilizadas em repositórios públicos de contas específicas do GitHub.

Durante a execução do pipeline, são feitas requisições autenticadas, utilizando os métodos GET, POST, PUT e DELETE, com tratamento de erros e paginação. Os dados extraídos são transformados em DataFrames com a biblioteca pandas e exportados para arquivos CSV. Além disso, o projeto inclui a criação, atualização e exclusão de repositórios via API, com o código estruturado seguindo os princípios da Programação Orientada a Objetos (POO).

## Conteúdo

### Módulo 1: Conhecendo a biblioteca Requests
◻️ Trabalhando com WSL;

◻️ Configurando o ambiente virtual com pip e venv;

◻️ Instalando a biblioteca Requests do Python;


### Módulo 2: Extraindo os dados
◻️ Gerando token de autenticação no Github;

◻️ Realizando requisições autenticadas via GET;

◻️ Extraindo dados da API do GitHub;

◻️ Utilizando a técnica de paginação;

◻️ Identificando os status code;

◻️ Aplicar tratamento de erros ao fazer requisições.

### Módulo 3: Transformando os dados
◻️ Percorrendo listas e dicionários;

◻️ Manipulando e estruturando dados no formato JSON;

◻️ Utilizando a biblioteca Pandas para criar DataFrames;

◻️ Transformando os dados utilizando a biblioteca Pandas;

◻️ Salvando os dados no formato CSV utilizando o método to_csv.


### Módulo 4: Armazenando os dados
◻️ Executando requisições POST;

◻️ Criando um repositório no GitHub através da biblioteca Requests;

◻️ Codificando arquivos em base64;

◻️ Fazendo o upload de um arquivo em um repositórios via requisição.

◻️ Realizando requisições PUT;

### Módulo 5: Estruturando o código
◻️ Criando classes em Python;

◻️ Otimizando a paginação;

◻️ Instanciando objetos;

◻️ Utilizando a requisição DELETE para excluir um repositório;

◻️ Estruturando e refatorando os códigos para Programação Orientada a Objetos.

## Como usar este repositório?
**Pré-requisitos**

- Python 3.8 ou superior

- Conta no GitHub

- Token de acesso pessoal do GitHub (necessário para autenticação)

**Estrutura do projeto:**

├── `classes/`

│   └── repository_data.py (lógica de extração de dados de repositórios)

│   └── repository_manipulate.py (lógica de manipulação de um repositório)

├── `notebooks/` 

│   └── exploracao.ipynb  (notebook para análise e exploração inicial dos dados)

├── `processed_data/`

│   ├── amazon.csv

│   ├── apple.csv

│   ├── netflix.csv

│   └── spotify.csv (dados coletados e processados para cada conta do GitHub via cada repositório)

├── `scripts/`

│   └── pipeline_data.py (pipeline principal de execução do projeto)

**Execução:**

1) Clone este repositório: `git clone https://github.com/pedromiguelsbs/repositories-requests`, `cd repositories-requests`
2) Crie e ative um ambiente virtual: `python -m venv venv`, `source venv/bin/activate`
3) Instale as dependências necessárias: `jupyter`, `pandas`, `requests` 
4) Execute o pipeline para coletar e processar os dados: `python scripts/pipeline_data.py`

## Contribuições
Se quiser sugerir melhorias ou compartilhar novos insights, fique à vontade para abrir uma _issue_ ou enviar um _pull request_.  

## Licença
Esse projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://github.com/pedromiguelsbs/repositories-requests/blob/main/LICENSE) para mais detalhes.
