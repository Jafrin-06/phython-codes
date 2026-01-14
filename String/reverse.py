#logical
string=input("Enter the String:")
reverse=""
for ch in string:
    reverse=ch+reverse
print("Reversed:",reverse)

#short
string=input("Enter the String:")
print(string[::-1])
