f=open("anagram.txt")
text=(f.read())
vowels="aeiouAEIOU"
count=0
for i in text:
   if i in vowels:
       count=count+1
print(count)
