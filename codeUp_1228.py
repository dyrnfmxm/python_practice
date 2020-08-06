h, w = map(float,input().split())
weight = (h-100)*0.9
#print(weight)
bmi = (w-weight) *100 / weight
#print(bmi)

if bmi <= 10:
    print("정상")
elif bmi >10 and bmi <= 20:
    print("과체중")
else:
    print("비만")
