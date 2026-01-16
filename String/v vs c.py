s=input("Enter the string:")
v=0
c=0
for ch in s:
    if ch in "AEIOUaeiou":
        v=v+1
    else:
        c=c+1
print("Vowels:",v)
print("Consonants:",c)
