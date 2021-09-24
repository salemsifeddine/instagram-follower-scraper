from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot():
    def __init__(self, email, password, username, max):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(executable_path=CM().install(), options=self.browserProfile)
        self.email = email
        self.password = password
        self.username = username
        self.max= max

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)
        self.browser.get('https://www.instagram.com/' + self.username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(10)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < self.max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == self.max):
                break
        return followers

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(10)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(10)
        else:
            print("You are already following this user")
    
    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(10)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(10)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")
    
    
    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()




browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
browser = webdriver.Chrome(executable_path=CM().install(), options=browserProfile)

def follow(email, password, username,max):
    browser.get('https://instagram.com/')
    browser.set_window_size(500, 950)
    time.sleep(10)
   
    username_field = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
    username_field.send_keys(email)

    find_pass_field = (
        By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
    WebDriverWait(browser, 50).until(
        EC.presence_of_element_located(find_pass_field))
    pass_field = browser.find_element(*find_pass_field)
    WebDriverWait(bot, 50).until(
        EC.element_to_be_clickable(find_pass_field))
    pass_field.send_keys(password)
    bot.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
    time.sleep(10)
    link = 'https://www.instagram.com/{}/'.format(username)
    browser.get(link)
    #browser.get('https://www.instagram.com/' + username)
    #followersLink = browser.find_element_by_css_selector('ul li a')
    #followersLink.click()
    #time.sleep(2)
    #followersList = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
    #numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    #followersList.click()
    #actionChain = webdriver.ActionChains(browser)
    #while (numberOfFollowersInList < max):
    #    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    #    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    #    print(numberOfFollowersInList)
    #        
    #followers = []
    #for user in followersList.find_elements_by_css_selector('li'):
    #    userLink = user.find_element_by_css_selector('a').get_attribute('href')
    #    print(userLink)
    #    followers.append(userLink)
    #    if (len(followers) == max):
    
    #        break
    #return followers
#bot = InstagramBot("salem_s36@yahoo.com","33025340Ss","en.algerie", 2)
#print( bot.signIn())

follow("salem_s36@yahoo.com", "33025340jojo", "cbum",20)