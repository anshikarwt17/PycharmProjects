choice= input("Enter 'f' if wanted to conevrt in fahrenheit or 'c' if  wanted to convert in celcius =")
if ((choice=="f") or( choice.upper== "F")):
    temp=int(input("Enter the temperature in celcius = "))
    Fahrenheit=(temp * 1.8) + 32
    print(" the temperaturein fahrenheit is ",Fahrenheit)
elif (choice=="c" or   choice.upper=="C"):
    temp=int(input("Enter the temperature in Fahrenheit = "))
    Celcius=(temp - 32) / 1.8
    print(" the temperaturein fahrenheit is ",Celcius)
else:
    print("invalid input")
