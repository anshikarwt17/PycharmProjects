lines=[]
print("Enter the lines or just press enter to finish: ")
while True:
    line= input()
    if line=="":
        break
    lines.append(line)
    print("/n you entered")

for line in lines:
    print(line)

