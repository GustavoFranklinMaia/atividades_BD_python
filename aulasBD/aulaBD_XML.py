import xml.etree.ElementTree as ET

class ExtratorDadosPassageiros:
    def __init__(self, arquivo_xml):
        self.arquivo_xml = arquivo_xml
        self.tree = ET.parse(arquivo_xml)
        self.root = self.tree.getroot()
    
    def numero_de_passageiros(self):
        return len(self.root.findall('passageiro'))
    
    def origens_e_destinos(self):
        origens = set()
        destinos = set()
        
        for passageiro in self.root.findall('passageiro'):
            origem = passageiro.find('origem').text
            destino = passageiro.find('destino').text
            
            origens.add(origem)
            destinos.add(destino)
        
        return list(origens), list(destinos)

if __name__ == "__main__":
    extrator = ExtratorDadosPassageiros("passageiros.xml")
    
    numero_passageiros = extrator.numero_de_passageiros()
    origens, destinos = extrator.origens_e_destinos()
    
    print(f'Número de Passageiros: {numero_passageiros}')
    print(f'Origens: {", ".join(origens)}')
    print(f'Destinos: {", ".join(destinos)}')
