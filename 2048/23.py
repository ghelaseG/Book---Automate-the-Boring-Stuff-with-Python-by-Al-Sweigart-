from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "/Users/georgeghelase/PycharmProjects/chromedriver"
browser = webdriver.Chrome(PATH)
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
