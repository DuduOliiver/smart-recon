import sys
import string
import json

lista_livros = []
dic_livros = {}

def monta_lista():
   with open('/home/kali/Desktop/automacao_recon/modulo1/json_complexo.json') as json_file:
      jsondata = json.load(json_file)
      for i in jsondata:
         for k in jsondata[i]:
            if('prateleira' in k):
               for prat01 in jsondata[i][k]:
                  print(prat01['titulo']) #printando json direto
                  lista_livros.append(prat01['titulo'])

def dicionario_livros():
   with open('/home/kali/Desktop/automacao_recon/modulo1/json_complexo.json') as json_file:
      jsondata = json.load(json_file)
      for i in jsondata:
         for k in jsondata[i]:
            if('prateleira' in k):
               for prat in jsondata[i][k]:
                  dic_livros['prateleira'] = k
                  dic_livros['titulo'] = prat['titulo']
                  dic_livros['genero'] = prat['genero']
                  print(dic_livros)

def mostra_lista():
   print(lista_livros)

def mostrar_ativos():
   with open('/home/kali/Desktop/automacao_recon/modulo1/json_complexo.json') as json_file:
      jsondata = json.load(json_file)
      for i in jsondata:
         if(i == "clientes"):
            for k in jsondata[i]:
               if(jsondata[i][k]['ativo'] == 'true'):
                  print('ativo: '+k)


def main():
   #monta_lista()
   #mostra_lista()
   dicionario_livros()
   mostrar_ativos()

if __name__ == '__main__':
   main()
