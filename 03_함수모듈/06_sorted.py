숫자들 = [3,1,1,3,4,5]
이름들=["민석","준순","지훈"]

print(sorted(숫자들))
print(sorted(이름들))
print(sorted(숫자들,reverse=True))
# 비교할 데이터가 단순해서 key가 없어도 된다. 정렬한 기준이 안에 있는 데이터들 뿐이기 때문

#이름 길이 순으로 정렬하고 싶다 ㄱ ㄴ ㄷ 순이 아닌 이름 길이로 정렬하고 싶다며

이름들=["김민석","박준순이야","박찬호야"]

print(sorted(이름들, key=lambda  x: len(x)))

def 길이순서기능(x):
    return len(x)

순서변경 = sorted(이름들, key=길이순서기능)
print(순서변경)

