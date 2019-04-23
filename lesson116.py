from selenium import webdriver

url = 'https://nid.naver.com/nidlogin.login'

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 로그인 하기
browser.get(url)
element_id = browser.find_element_by_id('id') # 아이드 텍스트 입력 상자
element_id.clear()
element_id.send_keys('idopark')
element_pw = browser.find_element_by_id('pw') # 비밀번호 텍스트 입력 상자
element_pw.clear()
element_pw.send_keys('*********')

browser.save_screenshot('website_c.png')

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()

# 메일페이지 열기
browser.get('https://mail.naver.com/')
browser.save_screenshot('website_d.png')

# 브라우저 종료하기
browser.quit()