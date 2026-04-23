
def problem1():
    과일들 = ["사과","바나나","포도"]
    print(len(과일들))

#problem1()

def multiply(a,b):
    a=int(input())
    b=int(input())
    return a*b

#print(f"{a}곱하기{b}는 {multiply(a*b)}입니다")






def welcome(name):
    print(f"{name}님, 환영합니다")

 ##welcome(name="김근육")

def average(a, b, c):

    return (a+b+c)/3

res = average(10,20,30)
print(f"평균은 {res}입니다")



def add(a+b):
    return a+b

        ## 기본값이 있는 매개변수가 ()안에 존재할 때 기본값 업는 매개변수 뒤에 위치하고
        #    매개변수 안에서 기본값이 없는 매개변수들이 맨 앞으로 위치해야 한다


def show(n):
    print(f"결과는 {n} 입니다")

show(add(7,8))
print(add(7,8))
