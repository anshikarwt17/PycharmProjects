import csv
with open("input.csv", mode='r' )as file:
    csvfile= csv.reader(file)

for lines in file:
    print(lines)

