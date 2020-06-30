def robot_action(x):
    #x = int(input())
    if x == 0:
        print("우회전")
    elif x > 1:
        print("점프")
    elif x < -1:
        print("유턴")
    else:
        print("전진")
