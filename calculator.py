class calculator:
    def addition(self):
        print(a+b)
    def substraction(self):
        print(a-b)
    def multiplication(self):
        print(a*b)
    def division(self):
        print(a/b)



print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")
choice = int(input("Enter your choice"))

a=int(input("enter first number: "))
b=int(input("enter second number: "))
obj = calculator()

if choice == 1:
    print(obj.addition())
elif choice == 2:
    print(obj.substraction())
elif choice == 3:
    print(obj.multiplication())
elif choice == 4:
    print(obj.division())

else:
    print ("pls enter the correct choise")
