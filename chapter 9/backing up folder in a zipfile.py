'''
backing up folder into zip file

'''

import zipfile, os

def backupToZip(folder):
    # backup all contents of folder to zip file
    folder = os.path.abspath(folder)
    number =1 
    while True:
        zipFilename = os.path.basename(folder)+"_"+str(number)+".zip"
        if not os.path.exists(zipFilename)
            break
        number += 1
        
# create the zip file
print('Creating %s...' % (zipFilename))
backupZip = zipfile.ZipFile(zipFilename, 'w')

# walk the entire folder and compress files in each folder
for foldername, subfolders, filenames in os.walk(folder): 
    print('Adding files in %s...' % (foldername))
    # add current folde rto zip file
    backupZip.write(foldername)
    # add all files in this folder to zip
    for filename in filenames:
        newBase / os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip') 
            continue # don't backup the backup ZIP files 
        backupZip.write(os.path.join(foldername, filename))
backupZip.close()
print('Done')

backupToZip("C:\\yourFolderName")
