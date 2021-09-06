from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            executable_path='/Users/rajani/Desktop/chromedriver')

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        


tb = TwitterBot('rajani', 'ldfsjf')
tb.login()
