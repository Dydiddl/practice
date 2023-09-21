print(1+1)
print(2-2)
print(3*3)
print(4/4)

print(5**5)
print(5%3)
print(5//3)

print(10 > 3)
print(10 <= 3)
print(10 >= 3)
print(5 <= 5)

print(10 == 10)
print(4 == 2)
print(10 != 10)
print(not 4!= 2)

print((3 > 0) and (3 < 7))
print((3 > 0) & (3 < 7))

print((3 > 0) or (3 < 7))
print((3 > 0) | (3 < 7))

print(5 > 4 > 3)
print(5 < 4 < 7)


print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))
print(round(5.5))
print(round(3.2))

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림    
print(sqrt(16)) # 제곱근

from random import *
print(random()) # 0.0 ~ 1.0 사이의 임의의 값을 생성
print(random()*10)
print(int(random()*10))
print(int(random()*10 + 1)) # 1부터 10까지

print(randrange(1, 46)) # 1 ~ 46미만의 값을 생성 - 로또 번호
print(randint(1, 45)) # 1과 45를 포함하는 번호 생성



