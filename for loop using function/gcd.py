def gcd(a,b):
    if(a<b):
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if(a%i==0 and b%i==0):
            gcd=i
    return gcd

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
print("G.C.D.=",gcd(a,b))
