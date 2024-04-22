test_string = "There are 289 apples for 4 persons"

# printing original string
print("The original string : " + test_string)


# getting numbers from string
res = []
x=test_string.split()
for i in x:
	if i.isnumeric():
		res.append(int(i))

# print result
print("The numbers list is : " + str(res))
