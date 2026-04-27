'''
python으로 가볍게 게임 만드는 라이브러리

화면에 도형/이미지 그리기
키보드/마우스 실시간 감지
소리 재생
애니메이션

설치방법 pip install pygame

'''
import pygame

pygame.init() #pygame. 초기세팅
화면 = pygame.display.set_mode((800,600))
pygame.display.set_caption("나의 게임") #창 제목
시계= pygame.time.Clock()                 # FPS 조절용

#게임 루흐 (tkinter 의 mainloop 같은거)
실행중=True
while 실행중:

    # 1. 이벤트 처리
    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT: # x버튼을 마우스로 클릭하면
            실행중=False

    화면.fill((0,0,0))     #화면 배경색 (r,g,b) 255 255 255 white
    pygame.display.flip()   #화면 갱신

    시계.tick(60)

pygame.quit