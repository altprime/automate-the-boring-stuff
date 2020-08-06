'''
excel to csv converter

convert all xls/xlsx files in the current working direcotry
to similarly named csv files

'''

import os, csv, openpyxl

for file in os.listdir('.'):
    if file.endswith('.xlsx'):
        wb = openpyxl.load_workbooks(file)
        
        for sheetName in wb.get_sheet_names():
            sheet = wb.get_sheet_by_name(selectName)
            nameSplice = file[:-5]
            csvFile = open(nameSplice + '_' + sheetName + '.csv', 'w', newline = '')
            csvWriter = csv.writer(csvFile)
            
            for rowNum in range(1, sheet.max_row + 1):
                row_data = []
                for colNum in range(1, sheet.max_column + 1):
                    row_data.append(sheet.cell(row = rowNum, col = colNum).value)
                    
                for row in row_data:
                    csvWriter.writerow(row)
            csvFile.close()
