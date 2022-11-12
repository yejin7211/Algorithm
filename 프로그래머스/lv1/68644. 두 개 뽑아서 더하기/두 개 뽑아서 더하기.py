def solution(nums):
    answer = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            answer.add(nums[i] + nums[j])
    answer = list(answer)
    answer.sort()
    return answer