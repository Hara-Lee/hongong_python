class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")

"""01과는 다르게 변수에 저장하게되면 '나중에 활용하겠다는 의미가 아닐까?
좀 더 지켜보자!'라고 생각하고 프로그램이 종료되는 순간까지 데이터를
메모리에서 제거하지 않습니다. 따라서 A,B,C가 생성된 후에 프로그램이
종료될 때 A,B,C 파괴가 일어납니다."""