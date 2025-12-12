class solution():
    def __init__(self,a):
        self.a=a
    def second_largest(self):
        largest = float('-inf')
        second = float('-inf')
        for n in self.a:
            if(n>largest):
                second=largest
                largest=n
            elif(n>second and n!=largest):
                second=n
        return second
a=[1,6,3,9,5,39,46,93]
objsec=solution(a)
print(objsec.second_largest())

