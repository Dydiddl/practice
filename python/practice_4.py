# 리스트

subway = [1,2,3]
print(subway)

subway = ["A", "B", "C"]
print(subway.index("B"))
subway.append("D")
print(subway)

subway.insert(1, "E")
print(subway)

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append("A")
print(subway)
print(subway.count("A"))


num_list = [5, 2, 3, 4, 1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

num_list = [5, 2, 3, 4, 1]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)