
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


# url_main = "https://everytime.kr/372165/p/"
url_test_first = 'https://everytime.kr/372165/p/1' # 아래도 변수 있다
browser.get(url_test_first)
time.sleep(1)  # 동적 요소 대기

articles = browser.find_elements_by_css_selector("#container > div.wrap.articles > article")
print(len(articles))

for index,article in enumerate(articles): # 게시판
      
      articles = browser.find_elements_by_css_selector("#container > div.wrap.articles > article")
      
      link = articles[index].find_element_by_css_selector('a')
      url_content = link.get_attribute('href')
      
      browser.get(url_content) # 1개 게시글 접속
      time.sleep(1)  # 동적 요소 대기

      # 이미지 스크린 샷. 개수대로. 없을수도 있음
      # 이미지 없는 게시글 continue 테스트 하고 오자.

      
      figures = browser.find_elements_by_css_selector("#container > div.wrap.articles > article > a > div > figure")
      if len(figures)==0:
            browser.get(url_content)
            time.sleep(1)
      else:
            for idx,figure in enumerate(figures):
                  #
                  figures = browser.find_elements_by_css_selector("#container > div.wrap.articles > article > a > div > figure")
                  img = figures[idx].find_element_by_css_selector('img')
                  url_src = img.get_attribute('src')

                  browser.get(url_src)      
                  time.sleep(1)

                  browser.save_screenshot('second'+str(idx)+'.png')

                  browser.get(url_content) # 다시 게시글 #요소에 접근할 수 없다는 에러가 났다     
                  time.sleep(1)


            browser.get(url_content)
            time.sleep(1)

      browser.get(url_test_first)
      time.sleep(1)




# 브라우저 종료
#browser.quit()






