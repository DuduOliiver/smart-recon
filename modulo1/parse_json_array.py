import sys
import string
import json

def parse():
   with  open('/home/kali/Desktop/automacao_recon/modulo1/json_array.json') as json_file:
      jsondata = json.load(json_file)
      for i in jsondata:
         for k in jsondata[i]:
            for t in k:
               print("Chave Externa [::] "+i+" [::] Chave Interna: "+t+" [::] Valor:"+k[t])
def main():
   parse()

if __name__ == '__main__':
   main()
