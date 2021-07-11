array = list(map(int,input().split()))

def quick_sort(array, start, end):
    if start >= end:    #원소가 1개인 경우 그냥 종료
        return

    pivot = array[0] # 피벗은 첫 번쨰 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
    reutrn quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
