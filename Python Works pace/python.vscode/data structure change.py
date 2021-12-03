# 자료구조의 변경
# 자료구조의 이름과 소괄호{}로 감싸주기만 하면 됨.

# 세트를 하나 만들고 , type() 을 이용하면 이 데이터가 어떤 형태인지 확인할 수 있습니다.
menu = {"커피", "우유", "주스"}
print(menu, type(menu))  # menu 의 type 정보 : set

menu = list(menu)  # 리스트 형태로 변환
print(menu, type(menu))  # menu 의 type 정보 : list

menu = tuple(menu)  # 튜플 형태로 변환
print(menu, type(menu))  # menu 의 type 정보 : tuple

# 다시 처음 상태인 세트로 돌아가겠습니다.
menu = set(menu)
print(menu, type(menu))