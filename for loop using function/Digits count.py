def countDigits(a):
    count=0
    for i in a:
        count=count+1
    return count
num=input("Enter the number:")
print(countDigits(num))
