import sys
import string
import json

dic_assetfinder = {}

def parse():
   with open('/home/kali/Desktop/automacao_recon/modulo2/assetfinder.txt') as file:
      for line in file:
         dic_assetfinder['subdomain'] = line.rstrip('\n')
         print(dic_assetfinder)

def main():
   parse()

if __name__ == '__main__':
   main()
