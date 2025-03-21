import requests
import base64
import os
from dotenv import load_dotenv

class RepositoryManipulate:

    def __init__(self, username):
        load_dotenv()
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token= os.getenv("GITHUB_TOKEN")
        self.headers = {'Authorization': f'token {self.access_token}',
                        'Accept': 'application/vnd.github.v3+json'}
        self.nome_repo = ''

    def create(self, nome_repo):
        self.nome_repo = nome_repo
        data = {
            'name': nome_repo,
            'description': 'Este repositório reúne os arquivos e materiais do curso de requisições com Python através da API do GitHub da Alura. O projeto envolve a construção de um pipeline ETL utilizando a biblioteca Requests integrada com a API do GitHub, abordando autenticação, paginação, métodos HTTP (GET, POST, PUT e DELETE) e POO.'
        }
        response = requests.post(f'{self.api_base_url}/user/repos', json=data, headers=self.headers)
        print(f'[Criando o repositório {nome_repo}] Status code: {response.status_code}')

    def upload(self, caminho_arquivo):
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)
        url = f"{self.api_base_url}/repos/{self.username}/{self.nome_repo}/contents/{caminho_arquivo}"
        data = {
            "message": "Adicionando um novo arquivo via PUT",
            "content": encoded_content.decode("utf-8")
        }
        response = requests.put(url, json=data, headers=self.headers)
        print(f'[Upload do arquivo {caminho_arquivo}] Status Code {response.status_code}')

    def delete(self):
        url = f'https://api.github.com/repos/{self.username}/{self.nome_repo}'
        response = requests.delete(url, headers=self.headers)
        print(f"{response.status_code}")