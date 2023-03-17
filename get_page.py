import json
import requests
import pandas
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def lambda_handler(event, context):
    ua = UserAgent()
    session = requests.Session()
    url = 'https://portal.stf.jus.br/processos/detalhe.asp?incidente=2226954'
    page_detalhes = session.get(url, headers={"User-Agent": str(ua.chrome)})
    page_detalhes.encoding = 'iso-8859-1'
    
    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(page_detalhes.content, 'html.parser')

    pagina_processo = {}
    tipo_extenso = soup.find('div', class_='processo-classe p-t-8 p-l-16')
    numerounico = soup.find('div', class_='processo-rotulo')
    tipo = soup.find('div',class_ = 'processo-titulo m-b-8')
    relator = soup.find('div', class_='processo-dados p-l-16')
    if tipo_extenso != None:
        pagina_processo["tipo_extenso"] = tipo_extenso.text.strip()
    if numerounico != None:
        pagina_processo["numerounico"] = numerounico.text.strip()
    if tipo != None:
        pagina_processo["tipo"] = tipo.text.strip()
    if relator != None:
        pagina_processo["relator"] = relator.text.strip()

    if True:
                
        url = 'https://portal.stf.jus.br/processos/abaAndamentos.asp?incidente=2226954&imprimir='
        ## make a request to the url with session.get with the enconding iso-8859-1


        page_detalhes = session.get(url, headers={"User-Agent": str(ua.chrome)})
        page_detalhes.encoding = 'iso-8859-1'

        # print(page_detalhes)

            # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(page_detalhes.content, 'html.parser')

            # Find all the list items in the HTML
        items = soup.find_all('li')
            # Loop through each list item and extract the information
        andamentos = []
        for item in items:
            dic = {}
            date = item.find('div', class_='andamento-data')
            name = item.find('h5', class_='andamento-nome')
            important = item.find('span',class_ = 'andamento-julgador badge bg-info')
            description = item.find('div', class_='col-md-9 p-0')
            if date != None:
                dic["dia"] = date.text.strip()
            if name != None:
                dic["nome"] = name.text.strip()
            if important != None:
                dic["importante"] = important.text.strip()
            if description != None:
                dic["descricao"] = description.text.strip()
            andamentos.append(dic)

        pagina_processo["andamentos"] = andamentos
      
    return pagina_processo
