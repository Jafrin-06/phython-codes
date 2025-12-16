class pairsum:
    def __init__(self,a):
        self.a=a
    def target(self):
        for i in range(len(self.a)):
            for j in range(i+1,len(self.a)):
                if self.a[i]+self.a[j]==5:
                    print("(",self.a[i], ",",self.a[j], ")")
a=[2, 4, 3, 5, 6, -2, 7]
obj=pairsum(a)
obj.target()
