n = input()
x = 0
y = 0
k = len(n)

if k < 20:
    for i in range(len(n)):
        if n[i] == "z":
            x += 1
        elif n[i] == "o":
            y += 1

    if 2*x == y:
        print("Yes")
    else:
        print("No")
else:
    print("No")