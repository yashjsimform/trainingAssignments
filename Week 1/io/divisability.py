n = int(input())
nums = input().split(" ")
nums = [int(i) for i in nums]

if nums[n-1] % 10 == 0:
    print("Yes")
else:
    print("No")