strName = input().split (" ")
matrix = [[] * int(strName[1]) for i in range (int(strName [0]))]
for matrLine in range(len(matrix)):
	matrix[matrLine]= input ().split(" ")

for matrLine in range(0, len(matrix)):
	for matrCol in range(0, len(matrix [matrLine])):
		print(matrCol)
		

	