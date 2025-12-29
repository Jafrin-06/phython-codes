n=int(input("Enter num of items:"))
list1=[]
for i in range(1,n+1):
    item=input("Enter the items:")
    list1.append(item)

list2={}
for i in list1:
    if i in list2:
        list2[i]=list2[i]+1
    else:
        list2[i]=1

count=0
maxFreq=None
for key in list2:
    if(list2[key]>count):
        count=list2[key]
        maxFreq=key
print("Most Repeating:",maxFreq)

    
