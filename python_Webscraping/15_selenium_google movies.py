import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
#  ,"Accept-Language":"ko-KR,ko" 코드를 통해 한글 언어로 된 페이지를 요청할 수 있다.
#   >> 그러면 그 서버에서 만약 한글 페이지가 있으면 그걸로 반환해주고 없으면 그냥 기본 페이지를 준다.

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:  << 파일로 저장
#     f.write(res.text)
#     f.write(soup.prettify())  >> html 문서를 예쁘게 출력 가능

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)