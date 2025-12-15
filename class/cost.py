class costlier:
    def __init__(self,pro1,cost1,pro2,cost2):
        self.p1=pro1
        self.c1=cost1
        self.p2=pro2
        self.c2=cost2
    def compare(self):
        if(self.c1>self.c2):
            print(self.p1," is costlier than ",self.p2)
        elif(self.c1<self.c2):
            print(self.p2," is costlier than ",self.p1)
        elif(self.c1==self.c2):
            print(self.p1," is as cost as ",self.p1)
pro1=input("Enter first product name:")
cost1=int(input("Enter price:")) 
pro2=input("Enter second product name:") 
cost2=int(input("Enter price:"))
obj=costlier(pro1,cost1,pro2,cost2)
obj.compare()
