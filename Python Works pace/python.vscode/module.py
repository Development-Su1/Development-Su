# 서로 관련이 있거나 비슷한 기능을 하는 파이썬 문장들을 담고 있는 파일을 모듈(module)
# 필요한 것들끼리 부품처럼 잘 만드는 것을 모듈화(modularization) 

# 직접 모듈을 하나 만들어보도록 하겠습니다.
# 워크스페이스 내에 새로운 파이썬 파일을 하나 만들고 이름은 theater_module.py 로 지어줍니다. 
# 이 파일에는 사람 수에 따른 영화표 가격을 계산해주는 3개 함수를 정의할텐데요. 
# 각 함수는 사람 수를 의미하는 people 을 전달받으며 1인당 영화표 가격은 price() 함수에서는 일반 가격인 10,000원, 
# price_morning()에서는 조조 할인 가격인 6,000원, price_soldier()에서는 군인 할인 가격인 4,000원으로 계산하여 출력
def price(people):
    print("{0}명 일반 가격은 {1}원 입니다.". format(people, people * 10000))

def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.". format(people, people * 6000))

def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.". format(people, people * 4000))

# 우리가 쓰던 practice2.py에서 불러올 것임.
# 원래 사용하시던 파일 (ex: practice2.py) 에서 모듈을 사용해볼텐데,
# 주의할 점은 theater_module.py 파일과 이 모듈을 사용할 파일은 서로 같은 경로상에 있어야 한다는 것입니다.


# [모듈 사용 방법 2]
# from ~ import구문을 사용함
# 실행결과는 동일함.
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)


# 그런데 때로는 모듈 내에 정의된 모든 내용을 가져다 쓰지 않고 필요한 것만 가져다가 써야할 때도 있습니다. 
# 예를 들어 이미 군대를 전역한 사람이라면 군인 할인 가격에 해당하는 price_soldier()함수는 아무런 쓸모가 없다. 
# 이 때는 from ~ import 구문 뒤에 * 대신 사용하고자 하는 부분만 콤마(,)로 구분하여 적으면 됩니다. 
from theater_module import price, price_morning    # 모듈에서 일부만 가져다 사용
price(5)    # 이번에는 5명
price_morning(6)
price_soldier(7)    # import 하지 않았으므로 사용불가

# 실행시켜보니 price()와 price_morning() 은 정상적으로 결과가 출력되는데 
# price_soldier()부분은 import를 하지 않았으므로 정의되지 않은 이름이라고 하며 에러가 발생.


# from ~ import 구문에도 as 를 적용하여 별명을 지어보겠음.
# 만약 현재 군생활을 하고 있는 군인이라면 어떨까요? 
# 일반 가격 (10,000원)이나 조조 할인 가격 (6,000원)보다 군인 할인 가격 (4,000원)이 더 저렴하므로 
# price() 와 price_morning()을 사용할 필요 없이 항상 price_soldier()를 사용합니다. 
# 그런데 price_soldier()라는 이름이 조금 길고 어차피 다른 함수는 사용하지 않으므로 새로운 별명인 price를 사용
# from ~ import 구문에도 as 를 이용하여 별명을 지어줄 수 있습니다. 
# from ~ import 구문 뒤에 as price 를 적어주면 코드에서는 price() 라는 이름으로 모듈 내 함수에 접근할 수 있으며 
# 이 때 실제로 호출되는 함수는 theater_module 내의 price() 가 아닌 price_solder() 가 됩니다.
from theater_module import price_soldier as price     # price_soldier를 새로운 별명인 price로 사용
price(5)    # price_soldier를 호출

# [실행결과]
# 5명 군인 할인 가격은 20000원 입니다.
