import string
import xml.etree.ElementTree as ET
import sys

#carrega a arvore XML
tree = ET.parse('/home/kali/Desktop/automacao_recon/modulo1/xml_complexo.xml')
#carrega a raiz
root = tree.getroot()

def parse_xml():
   #define o nome da raiz para teste
   for i in root.iter('teste'):
      for y in i:
         #diferentes atributos que podemos obter de acordo com nosso XML
         #print(y)
         print(y.tag)
         print(y.text)
         print(y.attrib)

def main():
   parse_xml()

if __name__ == '__main__':
   main()
