# Write a Python Program to create a Class in which one method
# accepts a string from the User and another method prints it.



class student:
     
     def name (self):
          global n1
          n1 = input("enter your name : ")

         
     def display(self):
          print("name of the student is ",n1)

harash = student()
harash.name()  #method used to get the name 
harash.display() #method used to print the name 