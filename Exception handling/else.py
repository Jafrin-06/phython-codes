try:
    a=int(input("Enter the num 1:"))
    b=int(input("Enter the num 2:"))
    c=a/b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(c)
