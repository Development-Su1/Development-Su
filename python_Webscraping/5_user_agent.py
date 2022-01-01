import requests
url = "http://Hensuocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("Hensucoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

#  "User-Agent"를 해줌으로써 크롬과 같이 동일한 결과를 낼 수 있다.
