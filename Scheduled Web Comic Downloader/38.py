# python3! - Write a program that checks the websites of several web comics and auto- matically downloads the images
# if the comic was updated since the program’s last visit

import bs4, os, requests

folderName = 'web-comics' #creates directory to play in.
os.makedirs(folderName, exist_ok=True)

def check_for_update(comicUrl): #downloads comic image if not found already in directory.
    fileName = os.path.basename(comicUrl) #get image filename.

    if fileName in os.listdir(folderName): #check if today's comic is in directory.
        print('No updates today. Most recent comic is at %s.' % comicUrl)

    else: #download today's comic.
        print('Downloading %s...' % comicUrl)

        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join(folderName, fileName), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

def get_qwantz_comic():
    site = 'http://www.qwantz.com' #get today's comic's url

    res = requests.get(site) #get url text to parse for img
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comicElem = soup.select('.comic') # get image url
    comicUrlShort = comicElem[0].get('src')
    comicUrl = site + '/' + comicUrlShort

    if comicElem == 0: #confirm whether there is an img url
        print('Could not find comic element at %s.' % site)
    else: #begin download of image with url
        check_for_update(comicUrl)

def get_xkcd_comic():
    site = 'https://xkcd.com' #get today's comic's url

    res = requests.get(site) #get url text to parse for img
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comicElem = soup.select('#comic > img') #get image url
    comicUrlShort = comicElem[0].get('src')
    comicUrl = 'http:' + comicUrlShort

    if comicElem == 0: #confirm whether there is an img url
        print('Could not find comic element at %s.' % site)

    else: #begin download of img with url
        check_for_update(comicUrl)

get_qwantz_comic()
get_xkcd_comic()
