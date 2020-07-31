'''
spreadsheet to text

open a spreadsheet and write cells of col A into a text file
cells of col B into another text file
so on...

'''

import os,openpyxl

# load spreadsheet 
wb = openpyxl.load_workbook('useThisSpreadsheet.xlsx')
sheet = wb.active  # take up the active sheet.

# create list of filenames 
fileNames = ['1.txt','2.txt','3.txt','4.txt']

for i in range(len(fileNames)):
    txtFileObj = open(fileNames[i],'w')
    for j in range(sheet.max_row):
            c = i+1 # column addressed by number starting at A (1)
            r = j+1 # row addressed by numbers starting at 1
            txtFileObj.write(str(sheet.cell(row=r,column=c).value))
txtFileObj.close()
