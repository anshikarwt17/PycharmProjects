import string
str=input("Enter the string :")
cleaned_string=""
for char in str:
    if char not in string.punctuation:
        cleaned_string += char

print("cleaned string = ",cleaned_string)