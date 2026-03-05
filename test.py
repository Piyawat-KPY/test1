import os
stock = []
with open('CprE_Subject - CprE_Subject.csv') as f:
    for line in f:
        token = line.split(',')
        ourseCode = token[0]
        name = token[1]
        type = token[2]
        credits = token[3]
        semester = token[4]
        lecturer = token[5]
        stock.append((ourseCode, name, type, credits, semester, lecturer))

for idx, item in enumerate(stock):
    print(idx, item)

print(len(stock))
print("------------------------------")
data = "10123102"
for element in stock:
    if element[0] == data:
        print(element)
        print(f"{data}\t: {element[1]} course \nCredit \t\t: {element[3]}")
    
print("------------------------------")