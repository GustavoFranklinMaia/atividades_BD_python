#ATIVIDADE 03 - (XML) 23/08/23 

import xml.etree.ElementTree as ET

class ExtratorDadosPassageiros:
    def __init__(self, arquivo_xml):
        self.arquivo_xml = arquivo_xml
        self.tree = ET.parse(arquivo_xml)
        self.root = self.tree.getroot()
    
    def numero_de_passageiros(self):
        return len(self.root.findall('passageiro'))
    
    def origens_e_destinos_de_passageiros(self):
        dados_passageiros = []

        for passageiro in self.root.findall('passageiro'):
            nome = passageiro.find('nome').text
            origem = passageiro.find('origem').text
            destino = passageiro.find('destino').text
            
            dados_passageiros.append({
                'nome': nome,
                'origem': origem,
                'destino': destino
            })
        
        return dados_passageiros
    
if __name__ == "__main__":
    extrator = ExtratorDadosPassageiros('passageiros.xml')
    
    numero_passageiros = extrator.numero_de_passageiros()
    dados_passageiros = extrator.origens_e_destinos_de_passageiros()
    
    print(f'Número de Passageiros: {numero_passageiros}')
    
    for passageiro in dados_passageiros:
        print(f'Nome: {passageiro["nome"]}, Origem: {passageiro["origem"]}, Destino: {passageiro["destino"]}')
