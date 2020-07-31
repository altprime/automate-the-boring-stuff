'''
link verification

take a url and attempt to downlaoad linked pages on this site
program will flag pages that have a 404 not found status and print 
broken links

'''

import sys, webbrowser, requests, bs4, re, os

def linkVerification():
    url = sys.argv[1]

    # go to the given url
    res = requests.get(url)
    if res.status_code != requests.codes.ok:
        print("Problem Occured")
    else:
        # get page
        soup = bs4.BeautifulSoup(res.text)

        # get all links on page
        linkElements = soup.select("a")
        # print(linkElems)
        for i in range(len(linkElements)):
            link = linkElements[i].get("href")
            if link != None:
                if link.startswith("//"):
                    link = "https:" + link
                elif link.startswith("#"):
                    link = url + link
                elif not link.startswith("http"):
                    g = re.search("^(http(.*?)\.(.*?)\/)", url)
                    link = g.group(1) + link

                res = requests.get(link)

                try:
                    res.raise_for_status()
                    print(link + " - " + linkElements[i].getText())
                except Exception as ex:
                    print(ex)


linkVerification()