class vehicle:
    def __init__(self,capacity):
        self.capacity=capacity
    def fare(self):
        return(self.capacity*100)
class bus(vehicle):
    def fare(self):
        base_fare=self.capacity*100 
        maintenance_charge=base_fare*0.1
        total_fare=base_fare+maintenance_charge
        return total_fare
capacity=int(input("Enter the vehicle capacity:"))
obj=bus(capacity)
print(obj.fare())
