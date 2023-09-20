def profile(name, age, main_language):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_language))
    
profile("유재석", 20, "Python")
profile("김태호", 30, "C++")

# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=17, main_language="Python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_language))
    
profile("유재석", 100)
profile("김태호")
