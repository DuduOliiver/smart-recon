import sys
import string
import json
import requests

dic_httprobe = {}

def parse():
   with open('/home/kali/Desktop/automacao_recon/modulo2/httprobe.txt') as file:
      for line in file:
         dic_httprobe['url_original']=line.rstrip('\n')
         dic_httprobe['protocolo']=line.rstrip('\n').split(':')[0]
         print(dic_httprobe)
def main():
   parse()

if __name__ == '__main__':
   main()
