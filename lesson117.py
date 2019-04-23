from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://www.indischool.com/index.php?act=dispMemberLoginForm')
driver.implicitly_wait(3)

driver.find_element_by_id('uid').send_keys('doglee')
driver.find_element_by_id('upw').send_keys('*******')
driver.find_element_by_css_selector('.hi.button.button-primary.button-expand').click()
# driver.save_screenshot('website_a.png')

driver.get('https://www.indischool.com/libClass')
titles = driver.find_elements_by_css_selector('span.title-link')
print(titles)
for title in titles:
	print('-', title.text)

driver.quit()
# driver.save_screenshot('website_a.png')