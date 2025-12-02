def checkPrime(num):
    count=0
    for i in range(1,num):
        if(num%i==0):
            count=count+1
    if(count>1):
        return("Not a Prime Number!")
    else:
        return("Prime Number!")

a=int(input("Enter the number:"))
print(checkPrime(a))
