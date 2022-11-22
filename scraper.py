from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

#this will need to be changed to wherever you put the geckodriver
# can be found at https://github.com/mozilla/geckodriver/releases
geckodriver_location = '/home/ashleyx/installs/geckodriver'


url = 'https://twitter.com/i/bookmarks'


#starting up firefox
browser = webdriver.Firefox(executable_path=geckodriver_location)
# driver.delete_all_cookies()

browser.get(url)

#at this stage find the firefox window that opens up and login in

input('Press Enter to continue')

browser.get(url)

retry_attempt=0
retry_limit=5

previous_height = 0
current_height = browser.execute_script("return document.documentElement.scrollHeight")

#this bit is trying to scrool the page all the way down.
#sometimes twitter tries to defend itself by pretending something went wrong and gives you a 
# button to retry. in that case just manually click the button and scroll
while retry_attempt < retry_limit:
    if current_height != previous_height
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3) #im only giving 3 seconds for the next block to load assuming good internet
        retry_attempt = 0 # resetting retry count if page size changes
        previous_height = current_height
        current_height = browser.execute_script("return document.documentElement.scrollHeight")
    else:
        retry_attempt = retry_attempt + 1


bookmarks = browser.find_elements('xpath','//div[@data-testid="tweetText"]')
bookmarks[0].text

# realized twitter only keeps 9-ish tweets even if you scroll all the way down. it's actively modifying and not displying tweets way out of view.
