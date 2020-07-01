while True:
    s = input()
    if s == 'help':
        print("에코를 해주는 프로그램입니다.")
    elif s == 'quit':
        answer = input("정말 종료하시겠습니까? (Y/N)")
        if answer == 'Y':
            break
    else:
        print("{} {} {}".format(s, s, s))
        
