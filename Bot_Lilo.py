from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys 
import time

"""
print("a")
 
browser = webdriver.Chrome('chromedriver') 
print("a1")  

# for i in range(1): 
#     matched_elements = browser.get("https://search.lilo.org/?q=" + search_string + "&start=" + str(i)) 

time.sleep(1)
print("a2")

for i in range(1) :
    time.sleep(2)
    matched_elements = browser.get("https://search.lilo.org/?q=" + "Charles est le plus beau" + "&start=" + str(i)) 

time.sleep(10000)

"""



class full_auto_lilo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('chromedriver') 

    def login(self):
        bot = self.bot
        bot.get('https://www.lilo.org/?act=login')
        time.sleep(3)
        email = bot.find_element_by_id('inputPseudo')
        password = bot.find_element_by_id('inputPassword')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(6)

    def makesearch(self, recherche):
        bot = self.bot
        bot.get("https://search.lilo.org/?q=" + recherche + "&start=") 
        time.sleep(3)


ed = full_auto_lilo('YOUR_MAIL@mail.com', 'YOUR_PASSWORD')

ed.login()
for i in range(10): 
    ed.makesearch("Charles est le plus beau")