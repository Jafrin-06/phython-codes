class Employee:
    def __init__(self):
        self.name="Jafrin"
        self.salary=60000
        print("Name:",self.name," Salary:",self.salary)
    def increment(self,percent):
        new_salary=((percent/100)*self.salary)+self.salary
        self.salary=new_salary
        print("Name:",self.name," Salary:",self.salary)
print("Before salary hike:")
objemploy=Employee()

percent=int(input("Enter the increase percent:"))
print("After salary hike:")
objemploy.increment(percent)
