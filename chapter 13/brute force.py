'''
brute force pdf password breaker

say you have an encrypted pdf and you've forgotten the password
you remeber it was a single English word
use brute force attack


dictionary.txt file from http://nostarch.com/automatestuff/
this file contains over 44k english words

'''


import docx, PyPDF2, time

wordFile = open('dictionary.txt')
text = wordFile.read()
wordList = text.split('\n')

pdfFile = open('watermarkEncrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

for word in wordList:
    if pdfReader.decrypt(word) != 0:
        print(word)
        break
    elif pdfReader.decrypt(word.lower()) != 0:
        print(word.lower())
        break
    else:
        continue