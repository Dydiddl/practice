# 딕셔너리
cavinet = {3:"유재석", 100:"김태호"}
print(cavinet[3])
print(cavinet[100])

print(cavinet.get(3))
# print(cavinet[5]) <- 키가 없기 때문에 나오지 않음
print(cavinet.get(5))
print(cavinet.get(5, "사용 가능"))

print(3 in cavinet)
print(5 in cavinet)

# 새로운 손님
print(cavinet)
cavinet[3] = "김종국"
cavinet["C-20"] = "조세호"
print(cavinet)

# 간 손님
del cavinet["C-20"]
print(cavinet)

# 총 사용중인 key
print(cavinet.keys())

# 총 사용중인 value
print(cavinet.values())

# 총 사용중인 key와 value
print(cavinet.items())

# 목욕탕 매점
cavinet.clear()
print(cavinet)