# headless chrome
# selenium을 사용해서 웹스크래핑을 하다 보면 매번 브라우저를 직접 띄우면서 화면을 움직이다 보니까 메모리도 많이 잡아먹고 속도가 느린면도 있습니다.
# 화면을 볼 필요도 없고 일반 pc가 아닌 서버에서 웹 스크래핑 작업을 할 경우 브라우저를 띄우는 작업을 할 필요가 없다.
# 이럴 때 사용하는게 바로 headless 기능입니다. chrome에서는 headless chrome이라고 하는데 이것은 chrome without chrome이라고 합니다.
# 즉, chrome을 띄우지 않고 chrome을 쓸 수 있는 것입니다. 쉽게 말해서 백그라운드에서 동작하는 것이라고 보면 되는 것입니다.

from selenium import webdriver

options = webdriver.ChromeOptions()  
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")   # screenshout 화면을 screenshout 파일로 저장. 


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "  <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()
