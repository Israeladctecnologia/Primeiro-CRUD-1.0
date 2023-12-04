#import json             #Lembrar de Importa o

from classes.AbstractCrud import AbstractCrud

class Produto(AbstractCrud):
    def  __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    ''' Nâo será mais necessário ter o codigo aqui uma vez que essa classe as recebe da classe pai

    def detalhar(self):
        return self.__dict__            # Lembrar do return!, o self.__dict__ para poder repetir ele mesmo em lista.  
    def inserir(self):
                    
        try:        # Usar o tentar!
            with open('db/produtos.json') as file:      #Vai tentar abrir a leitura do arquivo em json 
                lista = json.load(file)
        except Exception:
            lista = []   #Se não tiver o arquivo ira criar uma lista vazia

        lista.append(self.detalhar())       # Vai add a lista o self.__dict__

        with open('db/produtos.json', 'w') as file:           # Vai escrever na lista 'w' do arquivo
            json.dump(lista, file, indent= 4)    #  Ultima except, cria o arquivo como uma lista , com a var file no formato indent = 4

        print('Registro cadastrado com sucesso.')
    '''


