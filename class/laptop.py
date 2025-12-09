class laptop:
    def __init__(self):
        self.brand="Dell"
        self.ram="8GB"
        self.storage="512GB"
        print("Brand:",self.brand," RAM:",self.ram," Storage:",self.storage)
        
    def upgrade_ram(self,new_ram):
        self.ram=new_ram
        print("Updated!")
        print("Brand:",self.brand," RAM:",self.ram," Storage:",self.storage)
        
print("Default")
objdell=laptop()
new_ram=input("Enter the updated RAM:")
objdell.upgrade_ram(new_ram)
