str1 = input("Enter any string : ")
prefix = input("Enter prefix : ")
suffix = input("Enter suffix : ")
if str1.startswith(prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not starts with the prefix '{prefix}'.")
if str1.endswith(suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not ends with the suffix '{suffix}'.")