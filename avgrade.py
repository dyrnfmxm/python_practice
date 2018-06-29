score1 = int(input("점수를 입력하시오."))
score2 = int(input("점수를 입력하시오."))
average = (score1+score2)/2

if average >= 90:
    print("A")
elif average >=80:
    print("B")
elif average >=70:
    print("C")
elif average >=60:
    print("D")
else:
    print("F")
