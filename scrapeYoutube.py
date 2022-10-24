import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

listOfLinks = []

#pass in string
def scrapeVideos(query):
    query.strip().replace(" ","+")
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com/results?search_query="+query)
    # driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div').click()
    # a = driver.find_element(By.ID,"video-title")
    # driver.find_element(By.XPATH,'//*[@id="video-title"]').click()
    for i in range(10):
        html = driver.find_element(By.TAG_NAME,'html')
        html.send_keys(Keys.END)
        time.sleep(3)


    elemsLink = driver.find_elements(By.XPATH,"//a[@href]")
    elemsTitle = driver.find_elements(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')

    # for title in elemsTitle:
    #     print(title.get_attribute("video-title"))

    for links in elemsLink:
        youtubeWatchLinks = links.get_attribute("href")
        # print(elem.get_attribute("href"))
        if "watch?v=" in youtubeWatchLinks:
            if youtubeWatchLinks not in listOfLinks:
                listOfLinks.append(youtubeWatchLinks)
                print("HIT:  "+youtubeWatchLinks)

    print(listOfLinks)
scrapeVideos("jones barbeque foot massage ")

