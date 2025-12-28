n=int(input("Enter num of items:"))
list=[]
for i in range(1,n+1):
    item=input("Enter the items:")
    list.append(item)
print(list)
dict={}
for i in list:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
