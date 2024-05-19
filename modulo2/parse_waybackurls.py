import sys
import string
import json

dic_waybackurls = {}

def parse():
   with open('/home/kali/Desktop/automacao_recon/modulo2/waybackurls.txt') as file:
      for line in file:
         dic_waybackurls['protocolo']=line.rstrip('\n').split(':')[0]
         dic_waybackurls['url']=line.rstrip('\n')
         print(dic_waybackurls)

def main():
   parse()

if __name__ == '__main__':
   main()
