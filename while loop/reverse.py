def rev(n,reverse):
    while n>0:
        reverse=reverse*10+(n%10)
        n=n//10
    return reverse
    
num=int(input("Enter a number: "))
temp=0
reverse=rev(num,temp)
print(reverse)
while reverse>0:
    digit=reverse%10
    print(digit,end=" ")
    reverse=reverse//10
    
