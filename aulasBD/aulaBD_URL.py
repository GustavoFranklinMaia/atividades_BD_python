import requests
from bs4 import BeautifulSoup
import json

# URL do site de onde você deseja importar os dados
url = "https://openweathermap.org/api"

# Faz a solicitação HTTP
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parseia o HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selecione os atributos que você deseja extrair do HTML
    # Neste exemplo, estamos apenas simulando a seleção de 6 atributos fictícios
    atributo1 = soup.select_one('#atributo1').text
    atributo2 = soup.select_one('#atributo2').text
    atributo3 = soup.select_one('#atributo3').text
    atributo4 = soup.select_one('#atributo4').text
    atributo5 = soup.select_one('#atributo5').text
    atributo6 = soup.select_one('#atributo6').text

    # Crie um dicionário com os atributos selecionados
    data = {
        "atributo1": atributo1,
        "atributo2": atributo2,
        "atributo3": atributo3,
        "atributo4": atributo4,
        "atributo5": atributo5,
        "atributo6": atributo6
    }

    # Converta os dados em um arquivo JSON
    with open('dados.json', 'w') as arquivo_json:
        json.dump(data, arquivo_json, indent=4)
    print("Dados exportados para dados.json")
else:
    print("Erro na solicitação HTTP: ", response.status_code)
