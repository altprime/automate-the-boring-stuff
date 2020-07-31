'''
saving dowbnloaded files to hard drive

'''

import requests
reqs = requests.get('https://automatetheboringstuff.com/files/rj.txt')
reqs.raise_for_status()

playFile = open('RomeoandJuliet.txt', 'wb')
for bunch in reqs.iter_content(1000000): #value more than len(reqs.text)
    playfile.write(bunch)
playFile.close()
