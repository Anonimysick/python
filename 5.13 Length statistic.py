strName = input().split(" ")
lst = []
for i in strName:
	if len(i) != 0:
	 	lst.append(len(i))
	 	
#print(lst)

for i in lst:
#	print(i)
	print(i ,  lst.count(i))
