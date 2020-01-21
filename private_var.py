# 모듈을 가져옵니다.
import math

# 클래스를 선언합니다.
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

# 원의 둘레와 넓이를 구합니다.
circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

# __radius에 접근합니다.
print("# __radius에 접근합니다.")
print(circle.__radius)

# 클래스 내부에서 __radius를 사용하는것은 문제없지만, 클래스 외부에서
# __radius를 사용하려고 할 때는 그런 속성이 없다는 오류를 출력합니다.
# 이처럼 속성을 선언할 때 앞에 __를 붙이기만 하면 외부에서 사용할 수
# 없는 변수가 됩니다.