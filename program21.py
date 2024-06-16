def count_occurence(list,element):
    return list.count(element)

l1=[1,2,4,6,8,2,9,3,2,4,1]
print("the list is : ",l1)
ele=int(input("enter the number u want know its occurence = "))
print("the no. of occurence of ",ele,"is",count_occurence(l1,ele))

