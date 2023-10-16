from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#driver_path = "C:/Program Files/Google/Chrome/Application/chrome"


opt = Options()

#driver = webdriver.Chrome(executable_path= driver_path)
driver = webdriver.Chrome(options = opt)


url = "https://www.crunchbase.com"

driver.get('url')
#driver.find_element(By.ID, "input").send_keys(url)
#input
#//*[@id="input"]