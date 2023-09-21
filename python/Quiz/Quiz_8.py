class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

propert1 = House("강남", "아파트", "매매", "10억", "2010년")
propert2 = House("마포", "오피스텔", "전세", "5억", "2007년" )
propert3 = House("송파", "빌라", "월세", "500/50", "2000년")

property_list = [propert1, propert2, propert3]
print("총 {0}대의 매물이 있습니다.".format(len(property_list)))
for house in property_list:
    house.show_detail()



## gpt 친구가 만들어 줌
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.set_price(price)
        self.set_completion_year(completion_year)

    def set_price(self, price):
        try:
            # 가격을 정수로 변환하여 저장
            self.price = int(price)
        except ValueError:
            print("가격은 유효한 숫자여야 합니다.")
            self.price = None

    def set_completion_year(self, completion_year):
        try:
            # 완공 연도를 정수로 변환하여 저장
            self.completion_year = int(completion_year)
        except ValueError:
            print("완공 연도는 유효한 연도여야 합니다.")
            self.completion_year = None

    def show_detail(self):
        print(f"위치: {self.location}, 유형: {self.house_type}, 거래 유형: {self.deal_type}, 가격: {self.get_formatted_price()}, 완공 연도: {self.completion_year}")

    def get_formatted_price(self):
        if self.price is not None:
            return f"{self.price // 10000}억 {self.price % 10000}만원"
        else:
            return "가격 정보 없음"


propert1 = House("강남", "아파트", "매매", 1000000000, 2010)
propert2 = House("마포", "오피스텔", "전세", 500000000, 2007)
propert3 = House("송파", "빌라", "월세", "500/50", "2000")

property_list = [propert1, propert2, propert3]
print(f"총 {len(property_list)}대의 매물이 있습니다.")
for house in property_list:
    house.show_detail()
