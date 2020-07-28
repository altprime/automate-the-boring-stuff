'''
renaming  files with american style dates to european style dates

'''

import shutil, os, re

# create a regex for matching american style
datePattern = re.compile(r"""^(.*?) ((0|1)?\d)- ((0|1|2|3)?\d)- ((19|20)\d\d) (.*?)$ """, re.VERBOSE)

# loop over files
for amerFilename in os.listdir('.'): 
	mo = datePattern.search(amerFilename)

# skip files without a date
if mo == None:
	continue

# get different parts of filename
beforePart = mo.group(1) 
monthPart = mo.group(2) 
dayPart = mo.group(4)
yearPart = mo.group(6) 
afterPart = mo.group(8)

datePattern = re.compile(r"""^(1) (2 (3) )- (4 (5) )- (6 (7) )- (8)$ """, re.VERBOSE)

# form euro style filename 
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# get absolute file paths
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename) 
euroFilename = os.path.join(absWorkingDir, euroFilename)

# rename files
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

'''
uncomment the following line after testing

shutil.move(amerFilename, euroFilename)
'''


