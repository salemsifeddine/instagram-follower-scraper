import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

# complete these 2 fields ==================
USERNAME = 'devell.py'
PASSWORD = '33025340Ss'
# ==========================================

usr = input('Put the username for scrapping followers from: ')

user_input = input(
    'Put how many followers you want to scrape (60-500 recommanded):')
TIME = 0.069 * int(user_input)


def scrape(username):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    mobile_emulation = {
        "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/83.0.1025.133 Mobile Safari/535.19'
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)

    bot.get('https://instagram.com/')
   # bot.set_window_size(500, 950)

    connecte= WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Se connecter')]")))
    connecte.click()


    

    time.sleep(5)
    print("Logging in...")
    
    
    username = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


    username.clear()
    password.clear()


    username.send_keys("devell.py")
    password.send_keys("33025340jojo")


    log_in = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    log_in.click()

    time.sleep(5)

    not_now2= WebDriverWait(bot, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Plus tard')]")))
    not_now2.click()

    link = 'https://www.instagram.com/{}/'.format(usr)
    bot.get(link)
    time.sleep(5)

    bot.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()

    time.sleep(3)
    print('Scrapping...')
    for i in range(round(TIME)):
        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(3)

        followers = bot.find_elements_by_xpath(
            '//*[@id="react-root"]/section/main/div/ul/div/li/div/div[1]/div[2]/div[1]/a')

        urls = []

        # getting url from href attribute in title
        for i in followers:
            if i.get_attribute('href') != None:
                urls.append(i.get_attribute('href'))
            else:
                continue

    print('Converting...')
    users = []
    for url in urls:
        user = url.replace('https://www.instagram.com/', '').replace('/', '')
        users.append(user)

    print('Saving...')
    f = open('followers.txt', 'w')
    s1 = '\n'.join(users)
    f.write(s1)
    f.close()


scrape(usr)
