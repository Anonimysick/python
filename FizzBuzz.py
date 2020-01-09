strName = input()
markA = 0
listName = strName. split (" ")
for index in listName:
	if(index == "A"):
		markA = markA + 1
result = float(round((markA/len(listName)),2))
print('%.2f' % result)
