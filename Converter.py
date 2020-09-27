strName = input().split(" ")
number = float(strName[0])
unitFrom = strName[1]
unitTo = strName[3]


def func(num, unitf, unitt):
    # print(num,unitf,unitt)
    result = 0
    if unitf in "mm":
        if unitt in "mm":
            result = num
        if unitt in "cm":
            result = float(num / 10)

    return result


res = func(number, unitFrom, unitTo)

print('%.2e' % res)

# print (number, unitFrom, unitTo)
