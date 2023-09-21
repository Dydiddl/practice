def std_weigt(height, gender) : # 키는 cm로 적어주세요
    if gender =='남자' :
        standard_weight = height/100 * height/100 * 22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, standard_weight))
    else :
        standard_weight = height * height * 21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, standard_weight))

print(std_weigt(180, '남자'))
print(std_weigt(155, '여자'))

def std_height(height, gender) :
    if gender == '남자' :
        return height * height * 22
    else :
        return height * height * 21
    
height = 175
gender = '남자'
weight = round(std_height(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

def calculate_standard_weight(height, gender):
    # 키를 미터 단위로 변환
    height_meters = height / 100.0
    
    if gender == "남자":
        standard_weight = height_meters * height_meters * 22
    elif gender == "여자":
        standard_weight = height_meters * height_meters * 21
    else:
        return "올바른 성별을 입력하세요."

    return round(standard_weight, 2)

# 사용자로부터 키와 성별을 입력받습니다.
height = float(input("키(cm)를 입력하세요: "))
gender = input("성별을 입력하세요 (남자 또는 여자): ")

# 표준 체중을 계산하고 출력합니다.
standard_weight = calculate_standard_weight(height, gender)
if isinstance(standard_weight, str):
    print(standard_weight)
else:
    print(f"{height}cm {gender}의 표준 체중은 {standard_weight}kg입니다.")
