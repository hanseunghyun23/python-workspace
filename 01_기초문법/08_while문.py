'''
while 조건:
조건이 True 인동안 계속 실행
break 나 return 을 만나면 무한반복을 중단


'''

while True: 
    text = input("종료하려면 q를 입력하세요 : ")

    if text=="q":
        print("반복을 종료합니다")
        break
    print("반복하고 있습니다")