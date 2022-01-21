# selenium
# selenium은 웹 페이지 테스트 자동화를 할 수 있는 가장 유명한 프레임워크.

import time
from selenium import webdriver

browser = webdriver.Chrome()  # "./chromedriver.exe"
# 다른 경로를 이용할 경우 ()안에 그 경로 정보를 입력해줘야 함  
# >> Chrome 할 때 C는 대문자로 해준다.

# 1. 네이버 이동
browser.get("http://naver.com") 

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)  # 3초정도 기다렸다가 밑의 동작을 하도록 해줌.

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 7. html 정보 출력
print(browser.page_source)  # 지금 페이지에 있는 모든 html문서를 그대로 출력해줌.

# 8. 브라우저 종료
#browser.close()  # 현재 탭만 종료
browser.quit()   # 전체 브라우저 종료



# 테그로 정보 가져오기
elem = browser.find_element_by_tag_name("a") # >> 여러개의 element를 모두 가져오기 위해서는 element를 elements로 바꿔주면 됨.
elem
for a in elem:
    a.get_attribute("href")
# 위 코드를 작성하고 엔터 두번을 해줘야 끝남


# 다른 페이지로 이동 [daum으로 이동]
browser.get("http://daum.net")


# 검색창 옆에 검색 버튼 클릭
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/f.. ieldest/div/div/button[2]")
elem.click()


# 네이버 검색창
elem = browser.find_element_by_id("query")   # id를 name으로 해도 됨.
elem


# 글자를 Keys.Enter를 하기위해
from selenium.webdriver.common.keys import Keys
elem.send_Keys("자동차")
elem.send_Keys(Keys.ENTER)  # 위에서 입력한 자동차를 검색할 수 있음.


# 브라우저 이전 페이지로 이동
browser.back()


# 브라우저 다시 다음(앞으로)으로 이동
browser.forward()


# 브라우저 새로고침
browser.refresh()

