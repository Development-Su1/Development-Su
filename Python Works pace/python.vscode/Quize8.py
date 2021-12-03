# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# 매물 정보를 표시하기 위한 show_detail() 메소드에서는 멤버변수를 순서대로 출력합니다.
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__ (self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year 

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


# 여러 대의 매물에 대해 관리를 해야 하므로 houses 라는 이름의 리스트를 준비해두겠습니다.
# 그리고 각 매물정보를 전달하여 House 객체를 총 3개 생성합니다. 
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)


# 먼저 총 매물 수를 출력해볼까요?
# len() 함수를 이용하면 houses 리스트에 몇 개의 객체가 있는지 확인할 수 있으며
# 이 값이 바로 총 매물 수가 됩니다.
print("총 {0}대의 메물이 있습니다.". format(len(houses)))


# 반복문을 이용
for house in houses:
    house.show_detail()


# [총정리]
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, 
        self.price, self.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()