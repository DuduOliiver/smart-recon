import sys
import string
import json

with open('/home/kali/Desktop/automacao_recon/modulo1/json_basico.json') as json_file:
   jsondata = json.load(json_file)
   #print(jsondata['Key01']) #pegar chave individual
   for i in jsondata:
      print(i,'[::]',jsondata[i])

with open('/home/kali/Desktop/automacao_recon/modulo1/json_strings.json') as json_file:
   jsondata = json.load(json_file)
   for i in jsondata:
      print(i,'[**]',jsondata[i])

with open('/home/kali/Desktop/automacao_recon/modulo1/json_strings.json') as json_file:
   jsondata = json.load(json_file)
   for i in jsondata:
      print(i,'[-]',jsondata[i].split(' ')[2]) #com split

with open('/home/kali/Desktop/automacao_recon/modulo1/json_number.json') as json_file:
   jsondata = json.load(json_file)
   for i in jsondata:
      print(i,'[º]',jsondata[i])
