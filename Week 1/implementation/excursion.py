t = int(input())

for i in range(t):
    n,m,k = map(int, input().split())
    if n % k != 0:
        boyRoom = (n // k) + 1
    else:
        boyRoom = (n // k)
    
    if m % k != 0:
        girlRoom = (m // k) + 1
    else:
        girlRoom = (m // k)

    print(boyRoom + girlRoom)