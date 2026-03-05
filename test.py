import os
stock = []
with open('CprE_Subject - CprE_Subject.csv') as f:
    for line in f:
        stock.append(line.strip().split(','))

for idx, item in enumerate(stock):
    print(idx, item)

