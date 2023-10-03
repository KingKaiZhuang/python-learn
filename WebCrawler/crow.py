from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 指定您的Chrome瀏覽器位置
driver = webdriver.Chrome(options=options)

# 現在可以使用driver進行瀏覽器操作
driver.get("https://www.ptt.cc/bbs/Baseball/index.html")
# print(driver.page_source)
tags = driver.find_elements(By.CLASS_NAME,"title")
for tag in tags:
    print(tag.text)

print("---------------------------")
link = driver.find_element(By.LINK_TEXT,"‹ 上頁")
link.click()
tags = driver.find_elements(By.CLASS_NAME,"title")
for tag in tags:
    print(tag.text)

driver.close()