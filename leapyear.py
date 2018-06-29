year=0
year=int(input("계산 할 연도를 입력하시오"))
if(((year%4==0 )and (year%100!=0)) or (year%400==0)):
    print("%d 년은 윤년입니다"%year);
else:
    print("윤년이 아닙니다")
