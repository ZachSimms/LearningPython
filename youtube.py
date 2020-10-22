
from selenium import webdriver
# Firing up the browser to youtube
driver = webdriver.Chrome()
driver.get('https://youtube.com')

# Finding search box and typing text into it
search_box = driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys('David Goggins')

# Find and click the search button
search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()
