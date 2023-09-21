# https://docs.python.org/ko/3/py-modindex.html  <--- 여기서 공부

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else :
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")


# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime("%y-%m-%d %H:%ML%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td)