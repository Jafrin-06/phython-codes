def countDigits(a):
    count=0
    while a!=0:
        a=a//10
        count=count+1
    print(count)
num=int(input("Enter the number:"))
countDigits(num)
