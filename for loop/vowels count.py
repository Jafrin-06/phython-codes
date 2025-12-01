text = str(input("Enter a string: "))
vowels="aeiou"
count=0
for i in text:
   if i in vowels:
       count=count+1
print(count)
