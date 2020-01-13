#if조건문에서 None, 0, 0.0, 빈 컨테이너(빈 문자열, 바이트열, 리스트, 튜플, 딕셔너리 등)를
#제외하고는 모두 True로 변환됩니다

print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")