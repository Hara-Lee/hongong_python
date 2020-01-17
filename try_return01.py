# test() 함수를 선언합니다.
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

# test() 함수를 호출합니다.
test()

"""try 구문 내부에 return 키워드가 있는것이 포인트.
try 구문 중간에서 탈출해도 finally 구문은 무조건 실행됩니다.
따라서 함수 내부에서 파일 처리 코드를 깔끔하게 만들고 싶을 때
finally 구문을 활용하는 경우가 많습니다.
try 구문에서 원할 때 return 키워드로 빠져나가도 파일이
무조건 닫히기 때문입니다."""