from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



def Glogin(mail_address, password):

    # input Gmail
    driver.find_element(By.ID, "identifierId").send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()
    driver.implicitly_wait(10)
 
    # input Password
    driver.find_element(By.XPATH,
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "passwordNext").click()
    driver.implicitly_wait(10)




opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
 
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
    })
driver = webdriver.Chrome(options=opt)



#driver.get('https://meet.google.com/xby-zehb-ncf')
#driver.get('https://meet.google.com/?hs=197&authuser=0')
driver.get('https://duo.google.com/')
time.sleep(1)  # Ajouter un délai de 5 secondes pour permettre à la page de se charger
#driver.quit()

driver.find_element(By.XPATH,'//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/a/button').click()
#driver.implicitly_wait(2)


Glogin("evannrabeau@gmail.com","evann1205")
#time.sleep(60)

#ow3 > div.xTGfdf > div.cuAK0d > div:nth-child(1) > div > button > span
#driver.find_element(By.ID,"#ow3 > div.xTGfdf > div.cuAK0d > div:nth-child(1) > div > button").click
driver.find_element(By.XPATH,'//*[@id="ow3"]/div[3]/div[2]/div[1]/div/button').click()
time.sleep(5)

driver.find_element(By.XPATH,
        '//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/div/div/div[2]/span/div/div[1]/div/input').send_keys("dorian")
time.sleep(3)

############################
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/div/div/div[2]/span/div/div[2]/div[2]/div[5]/ul/li[1]').click()
time.sleep(3)


driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/div/div/div[2]/span/div/div[3]/div[3]/div[2]/div/button').click()
time.sleep(40)