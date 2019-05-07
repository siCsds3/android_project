
import time
from selenium import webdriver
import urllib.request as req
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER = "dqgsh35"
PASS = 'dareafat'


# Chome 드라이버 추출하기
browser = webdriver.Chrome()


###### 로그인 페이지에 접근하기############

url_login = "https://everytime.kr/login"
browser.get(url_login)
print('로그인 페이지에 접근')

#텍스트 박스에 아이디와 비밀번호 입력
e = browser.find_element_by_css_selector("#container > form > p:nth-child(1) > input")
# #container > form > p:nth-child(1) > input
e.clear()
e.send_keys(USER)

e = browser.find_element_by_css_selector('#container > form > p:nth-child(2) > input')
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인하기
form = browser.find_element_by_css_selector("#container > form > p.submit > input")
form.submit()
print("로그인 버튼을 클릭합니다")


###### 게시판 접근하기  ######


# url_main = "https://everytime.kr/372165/p/"
url_test_first = 'https://everytime.kr/372165'
# time.sleep(5)
browser.get(url_test_first)

# 요소가 보일 때까지 대기 ?
time.sleep(1)

articles = browser.find_elements_by_css_selector("#container > div.wrap.articles > article")
print(len(articles))

for article in articles:

      link = article.find_element_by_css_selector('a')
      print(link.get_attribute('href'))



# 브라우저 종료
browser.quit()






