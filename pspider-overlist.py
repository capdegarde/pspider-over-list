#!/usr/bin/python
from sys import argv
import subprocess
script, subs = argv

def main(sub_list):
    subdomains = open(sub_list, 'r')
    for line in subdomains:
        line = line.rstrip()
        output = line.strip('https://')
        subprocess.call(f'python ~/ParamSpider/paramspider.py -d {line} -o {output}',shell=True)

main(subs)
