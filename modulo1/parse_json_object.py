import sys
import string
import json

with open('/home/kali/Desktop/automacao_recon/modulo1/json_object.json') as json_file:
   jsondata = json.load(json_file)
   for i in jsondata:
      for k in jsondata[i]:
         print("[::] chave externa: "+i+" [::] chave: "+k+" [::] valor: "+jsondata[i][k])
