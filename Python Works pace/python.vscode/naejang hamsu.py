# 내장함수
# 내장 함수란 별도로 import를 하지 않고도 사용할 수 있도록 내장되어 있는 함수를 의미하는데요.
# 사용자의 입력을 받기 위한 input() 함수도 내장 함수 중 하나입니다. 
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다.". format(language))

# 프로그램을 실행시키고 "파이썬" 이라는 값을 입력하면 language 라는 변수에 저장을 했다가 
# print() 문을 통해서 출력을 합니다. 이 때 내장함수인 input()을 쓰기 위해 별도로 해줘야 하는 것은 아무것도 없었습니다.


# 내장함수인 dir() 함수에 대해 실습해보겠습니다.
# dir()은 어떤 객체를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 목적으로 사용할 수 있습니다.
# 만약 전달값으로 아무것도 넘기지 않는다면 현재 소스코드 범위 내에서 사용 가능한 모듈 또는 객체가 출력됩니다.

# 비교를 위해서 아무것도 import 하지 않았을 때의 dir() 함수 출력결과와
# random, pickle 모듈을 import 했을 때의 출력결과를 확인하는 코드를 작성합니다.
print(dir())
import random    # random 모듈 가져다 쓰기
print(dir())
import pickle    # pickle 모듈 가져다 쓰기
print(dir())

# >> 실행시켜보니 처음에는 기본 값들만 출력되고 
# import random 다음에는 random 모듈이, 
# import pickle 다음에는 pickle 모듈이 포함되어 코드 내에서 사용할 수 있음을 확인할 수 있습니다.


# random 모듈을 직접 전달값으로 설정하도록 하겠습니다.
import random
print(dir(random))

# >> 실행 결과 random 모듈 내에서 사용 가능한 모든 것들이 출력되는 것을 확인할 수 있습니다.
# randint, randrange, sample, shuffle 등 익숙한 이름들도 보이네요.


# 모듈이 아닌 리스트 자료구조를 하나 만들어서 확인해보겠습니다.
list = [1, 2, 3]
print(dir(list))

# >> 실행시켜보면 리스트에서 사용 가능한 변수와 함수 목록들이 보여집니다. 
# append, clear, count, extend, index, reverse, sort 등의 함수 이름도 확인할 수 있습니다.


# 문자열 변수를 하나 만들어서 확인해보겠습니다.
name = "Jo"
print(dir(name))

# >> name 이라는 문자열 변수에 대해서 대문자로 변경하는 upper, 소문자로 변경하는 lower, 
# 특정 문자를 찾는 find 등 다양한 기능을 사용할 수 있다는 것을 확인할 수 있습니다.
