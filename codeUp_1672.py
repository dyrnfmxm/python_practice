n, k = map(int,input().split())

quantity = n//k

if quantity > 9999:
    print("번호 초과 오류")
else:
    i = 1
    while i <= quantity:
        print("F-{0:04d}".format(i))
        i += 1
