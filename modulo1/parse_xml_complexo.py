import string
import xml.etree.ElementTree as ET
import sys

tree = ET.parse('/home/kali/Desktop/automacao_recon/modulo1/xml_complexo.xml')
root = tree.getroot()
dic_livros = {}

def parse_xml():
   for i in root.iter('livros'):
      for y in i:
         dic_livros['id']=y.attrib['id']
         for x in y:
            if x.tag == 'titulo': #validamos a tag quando queremos obter o valor em text
               dic_livros['titulo']=x.text
            if x.tag == 'resumo':
               dic_livros['resumo']=x.text
            if x.tag == 'genero':
               dic_livros['genero']=x.text
            if x.tag == 'autor':
               for a in x:
                  dic_livros['autor']=a.text
                  print(dic_livros)

def main():
   parse_xml()

if __name__ == '__main__':
   main()
