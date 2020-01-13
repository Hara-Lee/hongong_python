# 리스트 내부에 있는지 확인하기
# in/not in 연산자

list_a = [273, 32, 103, 57, 52]
string = input("입력> ")
string_num = int(string)
if string_num in list_a:
    print("{}은 리스트에 있습니다!".format(string_num))
else:
    print("{}은 리스트에 없습니다!".format(string_num))