#here I found 2 options a more complex one and shorter way (on Stackoverflow), and I realised that the main thing people are using is Selenium -> link to easily understand what it is and how to install it. 

import re, requests, threading, os
from bs4 import BeautifulSoup

def download_image(url):
    with open(os.path.basename(url), "wb") as f:
        f.write(requests.get(url).content)
    print(url, "download succesfully")

original_url = "https://www.flickr.com/search/?text=sea&view_all=1&page={}"

pages = range(1, 5000) #not sure how many pages here

for page in pages:
    concat_url = original_url.format(page)
    print("Now it is page", page)
    soup = BeautifulSoup(requests.get(concat_url).content, "lxml")
    soup_list = soup.select(".photo-list_photo-view")
    for element in soup_list:
        img_url = 'https:'+re.search(r'url\((.*)\)', element.get("style")).group(1)
        threading.Thread(target=download_image, args=(img_url,)).start()


#or you can use this second option with selenium
from selenium import webdriver
import re, requests, threading, os

#download image
def download_image(url):
    with open(os.path.basename(url), "wb") as f:
        f.write(requests.get(url).content)

PATH = "/Users/georgeghelase/PycharmProjects/chromedriver" #if you're PC user change this acordingly
driver = webdriver.Chrome(PATH)
original_url = "https://www.flickr.com/search/?text=sea&view_all=1&page={}"

pages = range(1, 5000) #choose randomly the pages

for page in pages:
    concat_url = original_url.format(page)
    print("Now it is page", page)
    driver.get(concat_url)
    for element in driver.find_elements_by_css_selector(".photo-list-photo-view"):
        img_url = 'https:'+re.search(r'url\(\"(.*)\"\)', element.get_attribute("style")).group(1)
        threading.Thread(target=download_image, args=(img_url, )).start()

#images will be downloaded in the same folder with the project!!
