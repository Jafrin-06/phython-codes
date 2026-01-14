#logical
sen=input("Enter the Sentence:")
largest=""
words=sen.split()
for w in words:
    if(len(w)>len(largest)):
        largest=w
print("Largest word:",largest)

#shortcut
sen=input("Enter the Sentence:")
largest=max(sen.split(),key=len)
print("Largest word:",largest)
