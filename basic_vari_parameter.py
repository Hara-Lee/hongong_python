def print_n_times(n=2, *values):
    # n 번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

# 함수를 호출합니다.
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍!")

#n에 "안녕하세요"가 들어가고 values에 나머지가 들어가기
#때문에 TypeError가 발생한다. 기본 매개변수의 의미가 사라짐.