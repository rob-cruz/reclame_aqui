import _0requisicao
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

#Em seguida, definimos uma função para extrair as informações de uma reclamação a partir de sua URL:


def extrair_dados_reclamacao(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(req.content, 'html.parser')

    titulo = soup.find('h1', {'class': 'sc-lzlu7c-3 hnjYTW'}).text.strip()
    empresa = soup.find('a', {'data-testid': 'company-page-link'}).text.strip()
    localizacao = soup.find('span', {'data-testid': 'complaint-location'}).text.strip()
    data_hora = soup.find('span', {'data-testid': 'complaint-creation-date'}).text.strip().split('\n')[0]
    id_reclamacao = soup.find('span', {'class': 'sc-lzlu7c-12 iwABCI'}).text.strip()
    categorias = [tag.text.strip() for tag in soup.find_all('div', {'class': 'sc-lzlu7c-11 gjquMH'})]
    mensagem = soup.find('p', {'class': 'sc-lzlu7c-17 fRVYjv'}).text.strip()
    dados_reclamacao = {
        'Título': titulo,
        'Empresa': empresa,
        'Localização': localizacao,
        'Data/Hora': data_hora,
        'ID da Reclamação': id_reclamacao,
        'Categorias': categorias,
        'Mensagem': mensagem
    }

    return dados_reclamacao