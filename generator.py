numbers = [1, 2, 3, 4, 5, 6]
temp = reversed(numbers)

# reverse() 함수의 결과는 제너레이터기 때문에
# 두 번째 반복문은 실행되지 않는다.

for i in temp:
    print("첫 번째 반복문: {}".format(i))
    print()

for i in temp:
    print("두 번째 반복문: {}".format(i))
    print()

for i in reversed(numbers):
    print("세 번째 반복문: {}".format(i))
    print()

for i in reversed(numbers):
    print("네 번째 반복문: {}".format(i))
    print()