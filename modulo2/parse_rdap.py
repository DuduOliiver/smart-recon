import sys
import string
import json
import requests

dic_openrdap = {}
dic_openrdap_ip = {}

def parse():
   r = requests.get('https://rdap.registro.br/domain/globo.com.br')
   json_rdap = json.loads(r.text)
   dic_openrdap['domain']=json_rdap['handle']
   for name in json_rdap['nameservers']:
      dic_openrdap['nameserver']=name['ldhName']
      dic_openrdap['dono']=json_rdap['entities'][0]['vcardArray'][1][2][3]
      dic_openrdap['responsável']=json_rdap['entities'][1]['vcardArray'][1][2][3]
      print(dic_openrdap)

def parse_tool():
   with open('/home/kali/Desktop/automacao_recon/modulo2/openrdap.json') as json_file:
      json_rdap = json.load(json_file) #load para leitura de arquivo, loads para leitura de string
      dic_openrdap_ip['blocoip']=json_rdap['handle']
      dic_openrdap_ip['startAddress']=json_rdap['startAddress']
      dic_openrdap_ip['endAddress']=json_rdap['endAddress']
      print(dic_openrdap_ip)

def main():
   parse()
   parse_tool()

if __name__ == '__main__':
   main()
