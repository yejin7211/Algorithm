def can_make_binarytree(arr):
    # 포화 이진트리가 만들어질 수 있는 최소 노드 개수로 맞추기
    level = 1
    while len(arr) > 2 ** level - 1:
        level += 1
    nodeCnt = 2 ** level - 1
    while len(arr) < nodeCnt:
        arr = [0] + arr
    
    midIdx = len(arr) // 2
    if arr[midIdx] == 1:  # 부모 노드가 1
        if can_make_binarytree(arr[:midIdx]) and can_make_binarytree(arr[midIdx+1:]):
            return 1
        return 0
    # 부모 노드가 0 => 자식 노드는 모두 0 이어야 한다.
    if sum(arr[:midIdx]) + sum(arr[midIdx+1:]) == 0:
        return 1
    return 0
    
def solution(numbers):
    answer = []
    for num in numbers:
        binary = []
        while num > 0:
            num, a = divmod(num, 2)
            binary.append(a)
        answer.append(can_make_binarytree(binary[::-1]))
    return answer