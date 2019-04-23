from selenium import webdriver

url = 'https://nid.naver.com/nidlogin.login'

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()

# 3초 대기하기
browser.implicitly_wait(3)

# url 읽어 들이기
browser.get(url)

# 화면을 캡처해서 저장하기
browser.save_screenshot('website_b.png')

# 브라우저 종료하기
browser.quit()