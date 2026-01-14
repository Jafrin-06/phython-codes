#logical
string=input("Enter the String:")
reverse=""
for ch in string:
    reverse=ch+reverse
if string.lower()==reverse.lower():
    print("Palindrome!")
else:
    print("Not a palindrome!")

#shortcut
string=input("Enter the String:").lower()
if(string==string[::-1]):
    print("Palindrome!")
else:
    print("Not palindrome!")
