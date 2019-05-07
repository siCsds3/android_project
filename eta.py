
import time
from selenium import webdriver



USER = "dqgsh35"
PASS = 'dareafat'


# Chome 드라이버 추출하기
browser = webdriver.Chrome()


'''########## 로그인 페이지에 접근하기 ##########'''

url_login = "https://everytime.kr/login"
browser.get(url_login)
print('로그인 페이지에 접근')

#텍스트 박스에 아이디와 비밀번호 입력
e = browser.find_element_by_css_selector("#container > form > p:nth-child(1) > input")
e.clear()
e.send_keys(USER)

e = browser.find_element_by_css_selector('#container > form > p:nth-child(2) > input')
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인하기
form = browser.find_element_by_css_selector("#container > form > p.submit > input")
form.submit()
print("로그인 버튼을 클릭합니다")





















'''########## 게시판 접근하기 ##########'''



# 이미지 없는 게시글에 접근
url_test_first = 'https://everytime.kr/372165/v/31585604'
browser.get(url_test_first)
time.sleep(1)


element = browser.find_elements_by_css_selector('#container > div.wrap.articles > article > a > div > figure')
print(len(element)==0) # True

# print 결과에 따라 예외처리문을 만든다



      







