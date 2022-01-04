n = int(input())
arr = input().split(" ")
arr = [int(i) for i in arr]
limits = []
upto = []
for i in range(0,n):
    temp = i
    steps = 0
    elemsRemain = n
    while elemsRemain >= 0:
        temp += 1
        elemsRemain = elemsRemain - temp
        steps += 1
    limits.append(steps-1)

for i in range(len(limits)):
    temp = 0
    sum1 = 0
    for j in range(i,limits[i]+1):
        sum1 = sum1 + j
    upto.append(sum1)
specialsums = []

for i in range(len(upto)):
    if upto[i] == 0:
        upto[i] = i + 1

for i in range(len(upto)):
    specialSum = 0
    print(i,upto[i])
    for j in range(i,upto[i]):
        specialSum += arr[j]
    specialsums.append(specialSum)

print(specialsums)

        