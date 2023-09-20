sentence = "나는 소년입니다."
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년입니다.
파이썬은 쉬워요.
"""
print(sentence3)

jumin = "123456-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])
print("뒤 7자리 : " + jumin[7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace('Python', 'Java'))

index = python.index("n")
print(index)
dindex = python.index("n", index + 1)
print(dindex)

print(python.find("Java"))
# print(python.index("Java"))
print("hi")

print(python.count("n"))

print("a" + "b")
print("a","b")

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는 {color}살이며, {age}색을 좋아해요".format(age = 20, color = "빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}식을 좋아해요.")

print("백문이 불여일견\n백견이 불여일타") #\n : 줄바꿈
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다")
print("저는 \'나도코딩\'입니다")

# \\ : 문장내에서 \
print("C:\\Python36\\python.exe")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rpine")

# \b : 백스페이스( 한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Redd\tApple")

# 퀴즈 3

site = "https://naver.com"
del_url = site[8:]
print(del_url)
del_dot = del_url[:5]
print(del_dot)
print( 
      "{}애서 생성된 비밀번호 : ".format(site)
      + del_dot[:3] 
      + str(len(del_dot)) 
      + str(del_dot.index("e")) 
      + "!"
)