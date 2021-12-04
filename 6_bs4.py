import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()   # 혹시라도 문제가 있으면 바로 종료할 수 있게 해줌

soup = BeautifulSoup(res.text, "lxml")  # soup가 모든 element를 가졌다는 것을 의미함 즉, 전체의 객체임
# print(soup.title)  << 타이틀 정보를 가져올 수 있다. (title element들을 전부 가져옴)
# print(soup.title.get_text())   << title element 안에 있는 글자만 가져올 수 있다.
# print(soup.a) # 모든 element를 가지고 있는 soup 객체에서 처음 발견되는 a element를 출력
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())

# print(rank1.next_sibling)  << 다음 랭크로 넘어갈 수 있음
# rank2 = rank1.next_sibling.next_sibling   // 시블링 (줄바꿈이 있을 수 있기 때문에 두번 해주는 것이다.)
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent) << li 테그의 부모인 ol 테그의 모든 값이 쭉 출력된다.

# rank2 = rank1.find_next_sibling("li")  << li에 해당하는 테그만 찾아줌
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# rank1.find_next_silbilngs("li")  << rank1을 기준을 다음 형제들을 모두 가져온다. (silblng에 s를 붙였기 때문)
# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마") 
# "독립일기-11화 밥공기 딜레마"에 해당하는 a 테그를 찾을 수 있음
print(webtoon)
