n, k = map(int, input().split())
p = list(map(int, input().split()))
f = 0
for i in range(n):
    c = p[i] % k
    for j in range(i+1,n):
            if c == p[j] % k:
                f += 1
print(f*2)

