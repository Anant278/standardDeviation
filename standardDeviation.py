import csv
import math
with open("data.csv", newline="") as x:
    reader = csv.reader(x)
    fileData = list(reader)
data = fileData[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    realMean = total/n
    return realMean

squaredList = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredList.append(a)

sum = 0
for j in squaredList:
    sum = sum + j
result = sum/(len(data)-1)
st = math.sqrt(result)
print(st)