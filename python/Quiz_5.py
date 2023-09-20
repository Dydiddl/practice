# import random
# total_passengers = 50
# matched_passengers = 0

# matched_passenger_info = []

# for passenger_number in range(1, total_passengers + 1):
#     travel_time = random.randint(5, 50)

#     if 5 <= travel_time <= 15:
#         matched_passengers += 1
#         matched_passenger_info.append(f"[ o ] {passenger_number} 번째 손님 (소요시간: {travel_time}분)")
#     else:
#         matched_passenger_info.append(f"[ ] {passenger_number} 번째 손님 (소요시간: {travel_time}분)")

# for info in matched_passenger_info:
#     print(info)

# print(f"총 탑승 승객: {matched_passengers} 명")



from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객: {0}명".format(cnt))
