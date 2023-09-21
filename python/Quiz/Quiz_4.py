from random import *
# user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14, 15, 16, 17, 18, 19, 20] # 20명 리스트 생성
user_list = list(range(1, 21))
print(user_list)

# 유저아이디 무작위로 섞기
shuffle(user_list)
print(user_list)

# 4명의 당첨자 선택
win = sample(user_list, 4)
# 출력문
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(win[0])) # 1명
print("커피 당첨자 : {0}".format(win[1:])) # 3명
print("-- 축하합니다 --")

