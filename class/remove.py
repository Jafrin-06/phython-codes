class remove:
    def __init__(self,a):
        self.a= a
    def remove(self):
        result = []
        for i in range(len(self.a)):
            if self.a[i] not in result:
                result.append(self.a[i])
        return result
a= [1, 2, 3, 2, 1, 4]
obj= remove(a)
print(obj.remove())
