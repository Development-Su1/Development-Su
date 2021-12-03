# from travel import *을 함으로써 travel 패키지의 모든 것을 가져다 쓰겠다고 하고 나서
# vietnamPackage 객체를 만들어보겠다.
from travel import *
trip_to = vietnam.vietnamPackage()
trip_to.detail()

# 실행시켜보니 다음과 같이 vietnam 이 정의되지 않았다며 에러가 발생하네요.
# >> NameError: name 'vietnam' is not defined

# * 을 쓴다는 것의 의미는 travel 이라는 패키지에 있는 모든 것을 가져다 쓰겠다는 것인데, 
# 실제로는 패키지를 만든 사람이 공개 범위를 설정해줄 수가 있답니다. 
# 즉, 패키지에 포함된 모듈 중에서 import 되기를 원하는 것만 공개를 하고 나머지는 비공개로 둘 수가 있는 거예요.
# travel 패키지를 만들 때 함께 생성했던 __init__2.py 파일을 열어 봅니다.
# __all__ 이라는 변수에 리스트 형태로 공개하려는 모듈 이름을 추가하면 해당 모듈에 대해 공개 설정을 할 수 있게 됨. 
# 이 때, __all__ 앞 뒤로 밑줄은 2번씩 적어주셔야 한다는 점 주의해주세요.


# __init__.py 파일을 저장하고 나서 원래 파일로 돌아와서 다시 코드를 실행해보겠습니다.
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원
# 그랬더니 이번에는 베트남 패키지 상품 정보가 잘 출력되는 것을 확인할 수 있습니다.


# 이번에는 ThailandPackage 객체를 만들어 보겠습니다.
# 이것도 위와 같은 방법으로 해결합니다.
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 실행결과 >> [태국 패키지 3박 5일]방콕, 파티야 여행(야시장 투어)50만원