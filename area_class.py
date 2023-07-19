class rectangle():
    def __init__(self,breadth,length):
        self.length = length
        self.breadth = breadth
    def area(self):
            return self.length*self.breadth 
a=int(input("enter length of rectangle: "))
b=int(input("enter breadth of rectangle: "))
obj=rectangle(a,b)
print("area of rectangle:",obj.area())
print()
