# 출석번호 1~4, 앞에 100을 붙이기로 함 -> 101, 102 ...
students = list(range(1,6))
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)