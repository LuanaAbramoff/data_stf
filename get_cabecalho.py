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
    
    
    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(page_detalhes.content, 'html.parser')
    
    
    # Find all the list items in the HTML
    items = soup.find_all('div')
    
    # Create an empty list to store the data
    dataf = {"tipo_extenso":[],"numerounico":[],"tipo":[],"relator":[]}
    data = {"tipo_extenso":"","numerounico":"","tipo":"","relator":""}
    
    # Loop through each list item and extract the information
    for item in items:
        tipo_extenso = item.find('div', class_='processo-classe p-t-8 p-l-16')
        numerounico = item.find('div', class_='processo-rotulo')
        tipo = item.find('div',class_ = 'processo-titulo m-b-8')
        relator = item.find('div', class_='processo-dados p-l-16')
        dataf["tipo_extenso"].append(tipo_extenso)
        dataf["numerounico"].append(numerounico)
        dataf["tipo"].append(tipo)
        dataf["relator"].append(relator)


    for key in dataf.keys():
        for i in dataf[key]:
            if i != None:
                data[key]=i.text.strip()
                

    return data

print(lambda_handler("",""))