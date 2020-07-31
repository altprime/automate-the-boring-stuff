'''
download files from the web

'''

import requests
reqs = requests.get('http://automatetheboringstuff.com/files/rj.txt')
reqs.status_code == requests.codes.ok
len(reqs.text) # should get 178981
print(reqs.text[:250])

# checking for errors
reqs = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    reqs.raise_for_status()
except Exception as exc:
    print("A problem occured: %s' % (exc))

s

