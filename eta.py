
import time
from selenium import webdriver



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

#  첫 번째 게시글로 test



# link = articles[0].find_element_by_css_selector('a')
link = articles[1].find_element_by_css_selector('a') # 여러 이미지가 있는 게시글 1개
# 가져온 links 출력해보기      
# print(link.get_attribute('href'))

      
# 가져온 게시글에 접속하기      
url_content = link.get_attribute('href')      
browser.get(url_content)      
time.sleep(1)


#################### 이미지 여러개  ###################### [css selector 구조가 다르니 주의]
# #container > div.wrap.articles > article > a > div.attaches.multiple > figure
figures = browser.find_elements_by_css_selector("#container > div.wrap.articles > article > a > div.attaches.multiple > figure")
#img = figures[0].find_element_by_css_selector('img')
#url_src = img.get_attribute('src')

for idx,figure in enumerate(figures):
      figures = browser.find_elements_by_css_selector("#container > div.wrap.articles > article > a > div.attaches.multiple > figure")
      img = figures[idx].find_element_by_css_selector('img')
      url_src = img.get_attribute('src')

      browser.get(url_src)      
      time.sleep(1)
#print(url_src)
      browser.save_screenshot('second'+str(idx)+'.png')

      browser.get(url_content) # 다시 게시글 #요소에 접근할 수 없다는 에러가 났다     
      time.sleep(1)


#################### 이미지 한개
#img_element = browser.find_element_by_css_selector('#container > div.wrap.articles > article > a > div.attaches.full > figure > img')
# img_element.click() # 클릭이 안되는 요소
#url_src = img_element.get_attribute('src')

##################### 이미지 스크린 샷
#browser.get(url_src)      
#time.sleep(1)
#print(url_src)
#browser.save_screenshot('second.png')


#for article in articles:
#
#      link = article.find_element_by_css_selector('a')
      # 가져온 links 출력해보기
#      print(link.get_attribute('href'))

      # 가져온 각 link에 접속하기
#      url_content = link.get_attribute('href')
#      browser.get(url_content)
#      time.sleep(1)



# 브라우저 종료
#browser.quit()






