# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: Forthrglory

import os
import re

def getPatch():
    file = open(os.getcwd() + '\\dict.txt').readlines()
    dict = {}
    for i in file:
        j = i.strip()
        j = j.split(' ')
        dict[j[0]] = j[1]
    return dict

def getSystem():
    info = os.popen("systeminfo").read()
    data = re.finditer(r'\[\d{2}\]: [a-zA-Z0-9]{8,9}', info)#:\S[a-zA-Z0-9]{9}
    dict = getPatch()
    for i in data:
        result = i.group().split(' ')
        result = result[len(result) - 1]
        if (dict.get(result) != None):
            dict.pop(result)
    for key in dict.keys():
        print(dict.get(key))

if __name__ == "__main__":
    getSystem()