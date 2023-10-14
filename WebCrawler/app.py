from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

service = Service(executable_path=r'./chromedriver.exe')
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(service=service, options=options)
chrome.get("https://www.facebook.com/")
