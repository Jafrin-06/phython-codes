class Anagram:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def check(self):
        if len(self.a)!=len(self.b):
            return False
        if self.a==self.b:
            return False
        for ch in self.a:
            if ch in self.b:
                return True
a=input("Enter the frst string:")
b=input("Enter the sec string:")
obj=Anagram(a,b)
print(obj.check())
