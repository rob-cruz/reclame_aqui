import _0requisicao
import _1extrai_dados
import _2extrai_urls
import time
from _2extrai_urls import extrair_urls_reclamacoes
from _1extrai_dados import extrair_dados_reclamacao
import pandas as pd
url_base = 'https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/'

start_time = time.time()
dados_totais = []
pagina_atual = 1

while True:
    pagina = f'{url_base}?pagina={pagina_atual}'
    urls_reclamacoes = extrair_urls_reclamacoes(pagina)

    #if not urls_reclamacoes:
    if not urls_reclamacoes:
        break

    for url in urls_reclamacoes:
        dados_reclamacao = extrair_dados_reclamacao(url)
        dados_totais.append(dados_reclamacao)
    #print(urls_reclamacoes)
    print(f'Página {pagina_atual} concluída.')


    pagina_atual += 1
    #print(dados_reclamacao

df = pd.DataFrame(dados_totais)
df.to_csv('reclamacoes_vivo.csv', index=False, encoding = "ISO-8859-1")


#Além disso, para medir o tempo de execução, podemos adicionar um timer no início e no final do script, e imprimir a diferença:




# código do script aqui

end_time = time.time()

print(f'Tempo de execução: {end_time - start_time:.2f} segundos')