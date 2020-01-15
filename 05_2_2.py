min_person = 2
max_person = 10
all_person = 100
memo = {}

def question(left_person, sit_person):
    key = str([left_person, sit_person])
    # 종료 조건
    if key in memo:
        return memo[key]
    if left_person < 0:
        return 0
    if left_person == 0:
        return 1

    # 재귀 처리
    count = 0
    for i in range(sit_person, max_person + 1):
        count += question(left_person - i, i)

    # 메모화 처리
    memo[key] = count

    # 종료
    return count

print(question(all_person, min_person))