t = int(input())
c = input()
s=[]

if t > 1:
    if "." not in c:
        print('NO')
    else:
        if "HH" not in c:
            print("YES")
            c = c.replace(".", "B")
            print(c)
        else:
            print('NO')
else:
    if c == "H":
        print("YES")
        print(c)
    elif c == ".":
        print("YES")
        c = c.replace(".", "B")
        print(c)
    else:
        print("NO")

