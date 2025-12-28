n=int(input("Enter num of items:"))
list1=[]
for i in range(1,n+1):
    item=input("Enter the items:")
    list1.append(item)
print(list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("Result:",list2)
