def move_disk(disk_num, start_peg, end_peg):
    print("Disk %d : %s to %s" % (disk_num, chr(start_peg+64), chr(end_peg+64)))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    other_peg = 6 - start_peg - end_peg
    if num_disks == 0:
        return
    elif num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, other_peg, end_peg)

disk_num = int(input())
hanoi(disk_num, 1, 3)
