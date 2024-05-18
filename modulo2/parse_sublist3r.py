import sys
import string
import json

dic_sublist3r = {}

def parse():
   with open('/home/kali/Desktop/automacao_recon/modulo2/sublist3r.txt') as file:
      for line in file:
         dic_sublist3r['subdomain']=line.rstrip('\n')
         print(dic_sublist3r)
def main():
   parse()

if __name__ == '__main__':
   main()
