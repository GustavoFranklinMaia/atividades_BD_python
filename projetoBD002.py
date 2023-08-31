import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import ttk


url = 'https://www.camara.leg.br/transparencia/gastos-parlamentares?legislatura=56&ano=2022&mes=&por=uf&deputado=&uf=PB&partido='

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tabela = soup.find()
    
    #! lista p/ armazenar dados
    dados = []
    
    for linha in tabela.find_all("tr"):
        colunas = linha.find_all("td")
        if len(colunas) >= 5:  
            dado1 = colunas[0].text.strip()
            dado2 = colunas[1].text.strip()
            dado3 = colunas[2].text.strip()
            dado4 = colunas[3].text.strip()
            dado5 = colunas[4].text.strip()
            #! Adicionar mais colunas conforme necessário

            dados.append([dado1, dado2, dado3, dado4, dado5])  #! Adicionar colunas conforme necessário

    #? Armazenando os dados coletados
    with open('dados_extraidos.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        
        #? Nome das colunas
        writer.writerow(['Nome do deputado', 'Partido', 'UF', "Despesas", "Mês"])  
        
        #? Escreve  no arquivo
        writer.writerows(dados)
    
    print("Dados extraídos e armazenados em 'dados_extraidos.csv'.")
else:
    print(f"Erro ao acessar a URL: {response.status_code}")


def carregar_dados():
    with open('dados_extraidos.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        dados = list(leitor)
    return dados
