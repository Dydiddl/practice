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