class number:
    def __init__(self,a):
        self.a=a
    def missing(self):
        n=len(self.a)+1
        expected_sum =n * (n + 1)//2
        print(expected_sum)
        actual_sum = 0
        for num in self.a:
            actual_sum=actual_sum+num
        return expected_sum-actual_sum
a= [1, 2, 4, 5]
obj=number(a)
print(obj.missing())
