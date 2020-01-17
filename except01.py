# try except 구문으로 예외를 처리합니다.
try:
    # 숫자로 변환합니다.
    number_input_a = int(input("정수 입력> "))
    # 출력합니다.
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    # 예외 객체를 출력해봅니다.
    print("type(exception):", type(exception))
    print("exception:", exception)

# 이와같이 예외가 발생할 때 이러한 정보를 메일 등으로 보내도록 해서
# 수집하면 이후에 프로그램을 개선하는 데 큰 도움이 됩니다.