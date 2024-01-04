import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def extrair_urls_reclamacoes(pagina):

    #print(pagina)
    #req = requests.get(pagina)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    req = requests.get(pagina, verify=False, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')


    urls_reclamacoes = []

    reclamacoes = soup.find_all('div', {'class': 'sc-1pe7b5t-0 eJgBOc'})

    for reclamacao in reclamacoes:
        url = reclamacao.find('a').get('href')
        url_completa = f'https://www.reclameaqui.com.br{url}'
        urls_reclamacoes.append(url_completa)

    #return urls_reclamacoes
    #print(url_completa)
    print(soup)