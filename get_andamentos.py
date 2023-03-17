import pandas as pd
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent



url = 'https://portal.stf.jus.br/processos/abaAndamentos.asp?incidente=2226954&imprimir='
ua = UserAgent()
session = requests.Session()

page_detalhes = session.get(url, headers={"User-Agent": str(ua.chrome)} )

# read the html file "andamentos.html" and store it in a variable
page_detalhes = open("andamentos.html", "r", encoding="utf-8")
# print(page_detalhes)

    # Parse the HTML using Beautiful Soup
soup = BeautifulSoup(page_detalhes, 'html.parser')

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
                    
print(andamentos)
