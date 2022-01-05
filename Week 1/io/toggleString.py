S = input()
s1 = ""
for i in range(len(S)):
    if S[i].isupper():
        s1 += S[i].lower()
    else:
        s1 += S[i].upper()

print(s1)