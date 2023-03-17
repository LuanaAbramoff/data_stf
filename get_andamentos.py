import pandas as pd
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


url = 'https://portal.stf.jus.br/processos/abaAndamentos.asp?incidente=2226954&imprimir='
ua = UserAgent()
session = requests.Session()

page_detalhes = session.get(url, headers={"User-Agent": str(ua.chrome)} )

    # Parse the HTML using Beautiful Soup
soup = BeautifulSoup(page_detalhes.text, 'html.parser')

    # Find all the list items in the HTML
items = soup.find_all('li')

    # Create an empty list to store the data
dataf = {"dia":[],"nome":[],"importante":[],"descricao":[]}
data = {"dia":"","nome":"","importante":"","descricao":""}

    # Loop through each list item and extract the information

for item in items:
    date = item.find('div', class_='andamento-data')
    name = item.find('h5', class_='andamento-nome')
    important = item.find('span',class_ = 'andamento-julgador badge bg-info')
    description = item.find('div', class_='col-md-9 p-0')
    dataf["dia"].append(date)
    dataf["nome"].append(name)
    dataf["importante"].append(important)
    dataf["descricao"].append(description)

for key in dataf.keys():
    for i in dataf[key]:
        if i != None:
            data[key]=i.text.strip()
        else:
            data[key] = ""
                    
print(data)
# Create a Pandas DataFrame from the data