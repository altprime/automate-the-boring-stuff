'''
regex search
open all .txt files in a folder and search for 
any line that matches user-supplied regex

'''

import re, os
 
textFiles = os.listdir('your/path/here')
 
print('What you wanna search for?')
userReg = str(input())
 
if userReg=='email':
    stringRegex = re.compile(r'[a-z0-9]+((\.|\_)[a-z0-9]+)*@[a-z0-9]+(\.[a-z0-9]+)*(\.[a-z0-9]{2,20})')
    #fileRegex = re.compile(r'\w+\.txt')
elif userReg=='phone':
    stringRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    #fileRegex = re.compile(r'\w+\.txt')
 
 
for file in textFiles:
    openFile = open('your/path/here' +file)
    readFile = openFile.readlines()
    for line in readFile:
        if stringRegex.search(line):
            print(stringRegex.search(line).group())
openFile.close()