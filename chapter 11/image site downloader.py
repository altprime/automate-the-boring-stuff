'''
image site downloader
go to a photo sharing site and search for a categor of image
and download all the resultant images


'''
import sys, re, os, requests, bs4


def downloadImage(siteURL, category):

    # create folder for category
    os.makedirs(category, exist_ok = True)

    res = requests.get(siteURL + "/search?q=" + category)
    # res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    reg = re.compile(r'(.*?)b(.jpg)$')
    # find list of all the images
    images = soup.select('#imagelist img')
    for im in images:
        if im.get("alt") == "":
            src = im.get("src")
            mo = reg.search(src)
            if mo != None:
                newSrc = mo.group(1) + mo.group(2)
                newSrc = "https:" + newSrc

                # save image to ./category
                imageFile = open(os.path.join(category, os.path.basename(newSrc)), "wb")
                res = requests.get(newSrc)
                res.raise_for_status
                for bunch in res.iter_content(100000):
                    imageFile.write(bunch)
                imageFile.close()

    print("Done")


url = "https://imgur.com/"
category = "dogs"
downloadImage(url, category)