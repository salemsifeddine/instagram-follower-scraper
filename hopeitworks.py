from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os
import wget
import time

user_input = input("enter number of followers . ")
TIME = 0.069 * int(user_input)
options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

mobile_emulation = {
        "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/83.0.1025.133 Mobile Safari/535.19'
    }
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(executable_path=CM().install(), options=options)

driver.get("https://www.instagram.com/")

connecte= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Se connecter')]")))
connecte.click()

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


username.clear()
password.clear()


username.send_keys("devell.py")
password.send_keys("33025340jojo")


log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
log_in.click()






not_now= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Plus tard')]")))
not_now.click()


not_now2= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Annuler')]")))
not_now2.click()

#not_now3= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Plus tard')]")))
#not_now3.click()

time.sleep(15)
driver.get("https://www.instagram.com/cbum/")


time.sleep(20)
#https://www.instagram.com/cbum/followers/
#/html/body/div[1]/section/main/div/ul/li[2]/a
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()

time.sleep(10)
for i in range(round(TIME)):
    ActionChains(driver).send_keys(Keys.END).perform()
    time.sleep(5)
    followers = driver.find_elements_by_xpath(
        '//*[@id="react-root"]/section/main/div/ul/div/li/div/div[1]/div[2]/div[1]/a')
    urls = []
    # getting url from href attribute in title
    for i in followers:
        if i.get_attribute('href') != None:
            urls.append(i.get_attribute('href'))
        else:
            continue

    users = []
    for url in urls:
        user = url.replace('https://www.instagram.com/', '').replace('/', '')
        users.append(user)

    print('Saving...')
    f = open('followers.txt', 'w')
    s1 = '\n'.join(users)
    f.write(s1)
    f.close()
#searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search")))
#searchbox.clear()
#