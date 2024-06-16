def sum_of_list(numbers):
    return sum(numbers)
    
l1=[]
n=int(input("How many numbers do you want in your list? = "))
for i in range(0,n):
    a=int(input())
    l1.append(a)

print("The list is= ",l1)
result= sum_of_list(l1)
print("the sum of all the numbers in the list: ",result)

