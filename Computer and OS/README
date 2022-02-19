import requests
from bs4 import BeautifulSoup

url="https://www.hackers.co.kr/?c=s_eng/eng_contents/B_others_wisesay&keywd=haceng_submain_lnb_eng_B_others_wisesay&logger_kw=haceng_submain_lnb_eng_B_others_wisesay"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print("[오늘의 한줄 영어명언]")
sentences = soup.find_all("div", attrs={"class":"text_en"})

print("[영어 명언지문 해석]")





