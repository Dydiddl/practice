print("Python", "Java","Javascript", sep=" vs ")

print("Python", "Java","Javascript", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "java", file=sys.stdout)
print("Python", "java", file=sys.stderr)

scores = {"수학": 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표 -> 001, 002, 003, 004, 005...
for num in range(1, 11):
    print("대기번호 : " + str(num))

for num in range(1, 11):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요  : ")
print(type(answer))
print("일력하신 값은 " + answer + "입니다.")
