def anagram(str1, str2):
    str1=str1.lower()
    str2=str2.lower()

    if len(str1)==len(str2):
        sorted_str1=sorted(str1)
        sorted_str2=sorted(str2)

        if sorted_str1== sorted_str2:
            return True
        else:
            False
    else:
        return False        

a= input("Enter the string:")
b= input("Enter the string:")
if anagram(a,b):
    print(f"{a} and {b} are anagrams.")
else:
    print(f"{a} and {b} are not anagrams.")