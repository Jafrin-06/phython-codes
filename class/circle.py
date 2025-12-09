class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*(self.radius**2)
        print("Area:",area)
    def circumference(self):
        print(self.radius)
        circum=2*3.14*self.radius
        print("Circumference:",circum)
radius=int(input("Enter the radius:"))
objcircle=circle(radius)
objcircle.area()
objcircle.circumference()
