import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.repository_data import RepositoryData
from classes.repository_manipulate import RepositoryManipulate

#PRÉ: Criando repositório
rm = RepositoryManipulate('pedromiguelsbs')
rm.create('python-requests')
#rm.delete() deleta o repositório

#EXTRACT
apple_repositories = RepositoryData('apple')
amazon_repositories = RepositoryData('amzn')
netflix_repositories = RepositoryData('netflix')
spotify_repositories = RepositoryData('spotify')

#TRANSFORM
apple_df = apple_repositories.create_df()
amzn_df = amazon_repositories.create_df()
netflix_df = netflix_repositories.create_df()
spotify_df = spotify_repositories.create_df()

#LOAD
apple_df.to_csv('processed_data/apple.csv')
amzn_df.to_csv('processed_data/amazon.csv')
netflix_df.to_csv('processed_data/netflix.csv')
spotify_df.to_csv('processed_data/spotify.csv')

#PÓS: Enviando para o repositório criado
rm.upload('processed_data/apple.csv')
rm.upload('processed_data/amazon.csv')
rm.upload('processed_data/netflix.csv')
rm.upload('processed_data/spotify.csv')
