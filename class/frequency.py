class Frequency:
    def __init__(self,a):
        self.a=a
        self.freq = {}
    def count_frequency(self):
        for num in self.a:
            if num in self.freq:
                self.freq[num]=self.freq[num]+1
            else:
                self.freq[num]=1
        return self.freq
a=[1, 2, 1, 3, 2, 1]
objfreq = Frequency(a)
print("Frequency:", objfreq.count_frequency())
