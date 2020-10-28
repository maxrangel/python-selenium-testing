from selenium import webdriver

# Init the web browser (Chrome version 86.0.4240.111)
chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Test if title contains the following text
assert 'Selenium Easy Demo' in chrome_browser.title

button = chrome_browser.find_element_by_class_name('btn-default')
button_text = button.get_attribute('innerHTML')

# Test if a button contains the following text
assert 'Show Message' in chrome_browser.page_source

# Get input and clear it, then add the 'I am cool text'
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am cool!')

# Click the button to display the button
button.click()

display_message = chrome_browser.find_element_by_id('display')

# Test if after clicking the button, the text is added to the display element
assert 'I am cool!' in display_message.text

chrome_browser.quit()
