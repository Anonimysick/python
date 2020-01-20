strName = input().split(" ")
lst = []
for i in strName:
    if len(i) != 0:
        lst.append(len(i))

# print(lst)
lst.sort()
for i in range(0, len(lst)):
    # print(lst[i])
    print(i, i+1)
    if lst[i] != lst[i+1]:
        print(lst[i], lst.count(lst[i]))
