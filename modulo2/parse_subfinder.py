import sys
import string
import json

dic_subfinder = {}

def parse():
   with open('/home/kali/Desktop/automacao_recon/modulo2/subfinder-json.json') as json_file:
      for line in json_file:
         json_line = line.rstrip('\n') #retirar quebra de linha
         jsondata = json.loads(json_line) #carregar json linha a linha
         dic_subfinder['subdomain']=jsondata['host']
         dic_subfinder['source']=jsondata['source']
         print(dic_subfinder)

def main():
   parse()

if __name__ == '__main__':
   main()
