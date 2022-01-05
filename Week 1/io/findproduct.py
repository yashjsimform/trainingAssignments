n = int(input())
nums = list(map(int, input().split(" ")))
ans = 0
const = 10**9 + 7

for i in range(n):
    if i == 0:
        ans = nums[0]
    else:
        ans = (ans * nums[i]) % (const)

print(ans)
    
