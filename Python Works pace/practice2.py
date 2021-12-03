# [모듈 사용 방법 1]
# 가장 기본적인 import 를 먼저 보겠습니다. 
# import구문을 쓸 때는 파일명 theater_module.py에서 확장자 .py 를 제외한 모듈 이름 theater_module을 그대로 적음. 
# import를 한 이후부터는 이 모듈에 정의한 함수를 사용할 수 있는데 모듈명 뒤에 점(.)을 찍고 나서 함수 이름을 적는다. 
# 3개 함수를 각각 호출하며 전달값은 3, 4, 5 로 해보겠습니다.
import theater_module     # theater_module 을 가져다가 사용
theater_module.price(3)   # 3명이서 영화 보러 갔을 때 가격
theater_module.price(4)   # 4명이서 조조 영화 보러 갔을 때 가격
theater_module.price(5)   # 5명의 군인이 영화 보러 갔을 때 가격

# [실행결과]
# 3명 가격은 30000원 입니다.
# 4명 조조 할인 가격은 24000원 입니다.
# 5명 군인 할인 가격은 20000원 입니다.


# 그런데 theater_module 이라는 이름이 다소 길어서 모듈을 사용할 때마다 긴 이름을 적자니 조금 불편합니다. 
# 이럴 때는 as 를 이용해서 모듈에 별명을 붙여줄 수 있습니다. 
# 영화는 영어로 movie 인데 이것도 길어 보이니 편의상 mv 라는 별명을 짓도록 하겠습니다. 
# import 구문 뒤에 as mv 를 붙여서 theater_module 이라는 이름을 이제는 mv 로 간편하게 호출할 수 있습니다. 
# 실행결과는 위와 동일하다.
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

