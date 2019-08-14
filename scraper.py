from selenium import webdriver
import time

driver = webdriver.Chrome()
robloxUrl = "https://www.roblox.com/games/?SortFilter=default&TimeFilter=0"
# browser.get(robloxUrl)

driver.get(robloxUrl)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(5)
images = driver.find_elements_by_class_name("game-card-thumb")
for image in images:
    print(image.get_attribute('src'))
len(images) # = 18 images
