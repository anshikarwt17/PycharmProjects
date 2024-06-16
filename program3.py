num=int(input("Enter the number:"))
a=num
fact=1
for i in range(1,a+1):

        fact=fact*i
        i+=1

print("the factorial of the ",num,"is",fact)