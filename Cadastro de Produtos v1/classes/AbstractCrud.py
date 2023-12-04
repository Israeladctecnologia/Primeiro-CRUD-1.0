import json

class AbstractCrud:  # Classe Pai

    def detalhar(self):
        return self.__dict__

    def inserir(self):
                    
        lista = self.lerArquivo()           # Chamando o self.lerArquivo para executar a função 

        lista.append(self.detalhar())       # Vai add a lista o self.__dict__

        with open('db/produtos.json', 'w') as file:           # Vai escrever na lista 'w' do arquivo
            json.dump(lista, file, indent= 4)    #  Ultima except, cria o arquivo como uma lista , com a var file no formato indent = 4

        print('Registro cadastrado com sucesso.')

    def listarTodos(self):
        
        lista = self.lerArquivo()

        for i, p in  enumerate(lista):      # Vai listar e enumerar os itens da lista
            print(f'{i} - {p}')

    def lerArquivo(self):   #Criada essa funçao depois podemos chama-la em outra função semprecisarmos repetir linhas do mesmo codigo
        try:        # Usar o tentar!
            with open('db/produtos.json') as file:      #Vai tentar abrir a leitura do arquivo em json 
                return json.load(file)          # Com o return podemos chamar em outra função
        except Exception:
            lista = []
