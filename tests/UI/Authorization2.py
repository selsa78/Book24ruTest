from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://s3.eu-central-1.amazonaws.com/qa-web-test-task/8544.html')
while True:
    driver.find_element_by_tag_name("a").click()