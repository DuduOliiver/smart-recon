import string
from unicodedata import name
import xml.etree.ElementTree as ET
import sys

dic_nmap = {}
dic_masscan = {}

tree = ET.parse('/home/kali/Desktop/automacao_recon/modulo2/masscan.xml')
root = tree.getroot()

def parse_xml():
   for i in root.iter('nmaprun'):
      for nmaprun in i:
         if nmaprun.tag=="host":
            for host in nmaprun:
               if host.tag=="address":
                  if(':' not in host.attrib['addr']):
                     dic_nmap['ipv4']=host.attrib['addr']
                     dic_nmap['addrtype']=host.attrib['addrtype']
                     dic_nmap['ip_other']=''
                  else:
                     dic_nmap['ip_other']=host.attrib['addr']
                     dic_nmap['addrtype']=host.attrib['addrtype']
                     dic_nmap['ipv4']=''
               if host.tag=="ports":
                  for port in host:
                     if(port.tag=='port'):
                        dic_nmap['protocol']=port.attrib['protocol']
                        dic_nmap['portid']=port.attrib['portid']
                        print(dic_nmap)

def parse_txt():
    with open('/home/kali/Desktop/automacao_recon/modulo2/masscan.txt') as file:
        for line in file:
            dic_masscan['address'] = line.rstrip('\n').split(' ')[5]
            dic_masscan['port'] = line.rstrip('\n').split(' ')[3].split('/')[0]
            dic_masscan['protocolo'] = line.rstrip('\n').split(' ')[3].split('/')[1]
            dic_masscan['state'] = line.rstrip('\n').split(' ')[1]
            print(dic_masscan)

def main():
   parse_xml()
   parse_txt()

if __name__ == '__main__':
   main()
