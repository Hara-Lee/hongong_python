class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

Test("A")
Test("B")
Test("C")

""" A가 생성되고 다음 줄로 넘어갈 때 이것을 변수에 저장하지 않으면
가비지 컬렉터는 이후에 활용하지 않겠다는 의미로 이해하고 메모리를
아끼기 위해 과감히 지워버립니다. 따라서 A가 생성되고, 사용하지
않을 것이 확실하므로 A를 제거해서 소멸하며, 이러한 과정이 반복됩니다."""