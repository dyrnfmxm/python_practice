s = input()
sad = happy = 0

for i in range(len(s)):
    if s[i] == ":":
        if s[i+1] == "-":
            if s[i+2] == ")":
                happy += 1
            elif s[i+2] == "(":
                sad += 1

if sad == 0 and happy == 0:
    print("none")
elif sad == happy:
    print("unsure")
elif sad > happy:
    print("sad")
elif sad < happy:
    print("happy")
