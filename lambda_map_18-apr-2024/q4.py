# Q Given list of employees. This list may contain repetitions. Find all unique employee names and print them as
# per order of second character in that name. Use lambda function and normal function both.

list1=["somedh","yash","manthan","harsh","pranjal", "yash", "harsh", "dhruva"]
set1=set(list1)
print(sorted(set1,key = lambda x : x[1:2:1]))

list2=list(set1)
#print(list2)
def second_char(list2: list):
     return list2[1:2:1]
print(sorted(list2,key=second_char)) 




