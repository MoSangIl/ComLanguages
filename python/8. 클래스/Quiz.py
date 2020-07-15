# Quiz
## 주어진 코드 활용 부동산 프로그램 작성하시오

# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")


##
building1 = House("강남", "아파트", "매매", "10억", "2010년")
building2 = House("마포", "오피스텔", "전세", "5억", "200년")
building3 = House("송파", "빌라", "월세", "500/50", "2000년")

buildings = []
buildings.append(building1)
buildings.append(building2)
buildings.append(building3)

print("총 {}대의 매물이 있습니다.".format(len(buildings)))

for building in buildings:
    building.show_detail()