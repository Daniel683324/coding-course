from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# from selenium.common.exceptions import StaleElementReferenceException

# C:\Users\daniel683324\Documents
import time
def multiplyer(number_one, number_two):
	return number_one * number_two


opts = Options()
opts.headless = False

assert opts.set_headless

browser = Chrome(
	executable_path =  'C:/Users/daniel683324/Documents/drivers/chromedriver.exe',
	options=opts)

browser.get('https://freerice.com/categories')
time.sleep(5)

# input_field = browser.find_element_by_tag_name('input')
# input_field.send_keys('')

list_of_categories = browser.find_elements_by_class_name('category-item')
multiplication_category = list_of_categories[21]
multiplication_category.click()
time.sleep(3)

for counter in range(0,20):
	question = browser.find_element_by_class_name('card-title')
	question_txt = question.text
	print (question_txt)
	question_num_list = question_txt.split(' x ')
	result = multiplyer(int(question_num_list[0]), int(question_num_list[1]))
	print (result)



	# first_ad.click()
	# time.sleep(4)

	answer_options = browser.find_elements_by_class_name('card-button')
	option_one = int(answer_options[0].text)
	option_two = int(answer_options[1].text)
	option_three = int(answer_options[2].text)
	option_four = int(answer_options[3].text)
	print (option_one)

	if (option_one == result):
		answer_options[0].click()

	elif (option_two == result):
		answer_options[1].click()

	elif (option_three == result):
		answer_options[2].click()

	elif (option_four == result):
		answer_options[3].click()

	time.sleep(3)	





browser.quit()