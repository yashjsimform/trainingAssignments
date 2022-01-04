code = str(input())
vowels = 'AEIOUY'

if ((int(code[0]) + int(code[1])) % 2) == 0:
    if code[2] not in vowels:
        if (int(code[3]) + int(code[4])) % 2 == 0:
            if (int(code[4]) + int(code[5])) % 2 == 0:
                if (int(code[7]) + int(code[8])) % 2 == 0:
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")
