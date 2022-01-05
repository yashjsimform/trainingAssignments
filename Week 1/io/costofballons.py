t = int(input())

for i in range(t):
    g, p = map(int, input().split(" "))
    n = int(input())
    first, second = 0, 0
    for i in range(n):
        one, two = map(int, input().split(" "))
        first += one
        second += two
    
    cost1 = g * first + p * second
    cost2 = p * first + g * second

    print(min(cost1,cost2))