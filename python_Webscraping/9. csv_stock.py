import csv    # csv 형태로 저장하기 위해
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
# utf-8이 아닌 utf-8-sig을 사용한 이유는 utf-8-sig가 엑셀에서 열어도 한글깨짐이 없기 때문.
# newline을 ""로 공백처리하면 줄만 바꿀 수 있음.
writer = csv.writer(f)   # csv로 파일 작성

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ...] >> 리스트 형태로 작성
# .split("\t")을 해주게 되면 tab로 구분된 것들이 리스트 형태로 들어가게 됨.
print(type(title))  # title의 type를 확인 [list여야 함.] 
writer.writerow(title)   # writerow는 리스트 형태로 넣어야 함.

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # 불필요한 것들을 제거하기 위해 .strip()을 사용했음.
        # print(data)
        writer.writerow(data)
