from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# from selenium.common.exceptions import StaleElementReferenceException

# C:\Users\daniel683324\Documents
import time

opts = Options()
opts.headless = False

assert opts.set_headless

browser = Chrome(
	executable_path =  'C:/Users/daniel683324/Documents/drivers/chromedriver.exe',
	options=opts)

browser.get('https://ecosia.org')
input_field = browser.find_element_by_tag_name('input')
input_field.send_keys('ads')
input_field.submit()
time.sleep(3)

list_of_ads = browser.find_elements_by_class_name('result-title-ad')
first_ad = list_of_ads[0]
first_ad.click()

time.sleep(4)


browser.quit()