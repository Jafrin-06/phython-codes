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
text="A man a plan a canal Panama"
obj=palindrome(text)
print(obj.check())
