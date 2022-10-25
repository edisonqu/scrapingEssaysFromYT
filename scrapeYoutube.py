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
        if "watch?v=" in youtubeWatchLinks and "t=" not in youtubeWatchLinks:
            video_id = youtubeWatchLinks.split("=")[-1]
            if video_id not in listOfLinks:
                listOfLinks.append(video_id)
                print("HIT:  "+youtubeWatchLinks)

    driver.quit()
    return listOfLinks
print(scrapeVideos("jones barbeque foot massage "))

