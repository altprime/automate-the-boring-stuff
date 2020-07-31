'''
clicking on 'im feeling lucky' on google search
opens the first page of search results
we'll open top 5
'''

import requests, sys, webbrowser, bs4
print('googling results...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# finding all the results // retrieving top results

soup = bs4.BeautifulSoup(res.text)
# open a browser tab for each result
linkElems = soup.select('.r a')
# top 5
numOpen = min(5, len(linkElems)) for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
