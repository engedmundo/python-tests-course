import requests

class Pessoa:
    def __init__(self, nome, sobrenome, dados_obtidos=False):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = dados_obtidos

    def obter_todos_os_dados(self):
        resposta = requests.get('https://www.google.com')    
        
        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'