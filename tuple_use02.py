# 튜플은 임시변수 없이 값의 교환이 가능하다. 
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

# 값을 교환합니다.
a, b = b, a
print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()