absent = [2, 5]
no_book = [7]
for student in range(1,11): # 1부터 10번까지의 번호
    if student in absent:
        continue  # absent에 있는 번호는 넘어가시오
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복문 탈출
    print("{0}, 책을 읽어봐".format(student))