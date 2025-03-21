import requests
import pandas as pd
import os
from dotenv import load_dotenv
from math import ceil

class RepositoryData:

    def __init__(self, owner):
        load_dotenv()
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token= os.getenv("GITHUB_TOKEN")
        self.headers = {'Authorization': f'token {self.access_token}',
                        'Accept': 'application/vnd.github.v3+json'}
    
    def list(self):
        repos_list = []
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)
        for page_num in range(1, num_pages+1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list

    def names(self, repos_list): 
        repo_names=[] 
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except: 
                     pass
        return repo_names

    def languages (self, repos_list):
        repo_languages=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo ['language'])
                except:
                    pass
        return repo_languages
    
    def create_df (self):
        repositories = self.list()
        names = self.names(repositories)
        languages = self.languages(repositories)
        df = pd.DataFrame({'name':names, 'language':languages})
        return df