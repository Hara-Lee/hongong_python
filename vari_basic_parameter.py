def print_n_times(*values, n=2):
    # n 번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

# 함수를 호출합니다.
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍!", 3)

#[]"안녕하세요", "즐거운", "파이썬 프로그래밍!", 3]
#을 두 번 출력하게 된다. 가변 매개변수가 우선시 되기 때문이다.