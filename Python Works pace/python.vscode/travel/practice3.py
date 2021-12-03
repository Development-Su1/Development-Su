# ThailandPackage 객체를 민들고 디테일 메소드 호출
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


# import구문을 사용할 떄는 그 대상이 모듈이나 패키지여야 함. (클래스나 함수는 import를 할 수 없음)
# 예를 들어 >> import travel.thailand.ThailandPackge


# 반면에 from ~ import구문을 이용하면 모듈, 패키지, 클래스, 함수 모두 이용할 수 있다.
# 이때는 import한 클래스 객체를 생성할 때 앞에서 했던 것과는 다르게 travel.thailand부분은 생략하고
# 클래스 이름인 ThailandPackage를 통해 접근 가능합니다.
from travel.thailand import ThailandPackage    # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
trip_to = ThailandPackage()    # travel.thailand부분은 생략
trip_to.detail()



# 이번에는 베트남 모듈을 해보도록 하겠습니다.
from travel import vietnam    # travel 패키지에서 vietnam 모듈 가져오기
trip_to = vietnam.vietnamPackag()   # travel 생략
trip_to.detail()


# import travel.vietnam
# trip_to = travel.vietnam.vietnamPackage()
# trip_to.detail()


# from travel.vietnam import vietnamPackage    
# trip_to = vietnamPackage()   
# trip_to.detail()