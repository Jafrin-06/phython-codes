# 1. Count frequency of each element (without using collections)
# Input:
# [1, 2, 1, 3, 2, 1]
# Output:
# {1:3, 2:2, 3:1}

class count:
    def __init__(self, a):
        self.a = a
    def freq(self):
        visited = []
        for i in range(len(self.a)):
            if self.a[i] in visited:
                continue
            count = 1
            for j in range(i + 1, len(self.a)):
                if self.a[i] == self.a[j]:
                    count=count+1
            visited.append(self.a[i])
            print(self.a[i], ":", count)
a = [1, 2, 1, 3, 2, 1]
obj=count(a)
obj.freq()
