class palindrome:
    def __init__(self, text):
        self.text = text
    def check(self):
        text=self.text.lower().replace(" ", "")
        rev=""
        for ch in text:
            rev=ch+rev
        if text==rev:
            return True
f=open("palindrome.txt")
text=f.read()
print(text)
obj=palindrome(text)
print(obj.check())
