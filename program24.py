num1= int(input("enter the 1st number ="))
num2=int(input("enter the 2nd number = "))
choice=input("enter the operator '+' for add,'-' for subtraction,'*' for multiplication,'/' for division = ")
if choice=="+" :
    print("the sum of two numbers:",num1+ num2)
elif choice=="-" :
    print("the difference of two numbers:",num1- num2)
elif choice=="*" :
    print("the product of two numbers:",num1* num2) 
elif choice=="/" :
    print("the quotient of two numbers:",num1/num2) 
else:
    print("invalid choice")
    