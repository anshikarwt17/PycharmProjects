def fib(n):
    
    if(n<0):
        print("please enter the positive number")
    elif(n==0):
        return n
    elif(n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
    

a=int(input("Enter the number:"))
print("the fibonacci series  : ")
for i in range(0,a+1):
    print(fib(i))
    