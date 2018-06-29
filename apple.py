apQuality = input("사과의 상태를 입력하시오")
apPrice =  int(input("사과의 가격을 입력하시오"))

if apQuality=="신선":
        if apPrice < 1000:
            print("사과를 10개 산다")

        else:
            print("사과를 5개만 산다")

else:
    print("사과를 사지 않는다")
    
