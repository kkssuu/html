import pygame
import random
########################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height= 640 #세로 크기
screen =pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('게임 이름')

#FPS
clock=pygame.time.Clock()
########################################################

#1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

bg=pygame.image.load('C:/Users/user/Desktop/Python/pygame_basic/background.png')

c=pygame.image.load('C:/Users/user/Desktop/Python/pygame_basic/character.png')
c_s=c.get_rect().size
c_w=c_s[0]
c_h=c_s[1]
c_x=screen_width/2-c_w/2
c_y=screen_height-c_h

e=pygame.image.load('C:/Users/user/Desktop/Python/pygame_basic/enemy.png')
e_s=e.get_rect().size
e_w=e_s[0]
e_h=e_s[1]
e_x=random.randint(0,screen_width-e_w)
e_y=(0)

to_x=0

c_sp=0.6
e_sp=10

running=True 
while running:
    dt=clock.tick(30) 
    
    '''
    if e_y==screen_height:
        e=pygame.image.load('C:/Users/user/Desktop/Python/pygame_basic/enemy.png')
        e_s=e.get_rect().size
        e_w=e_s[0]
        e_h=e_s[1]
        e_x=random.randint(0,screen_width-e_w)
        e_y=(0)
    '''

    if e_y>screen_height:
        e_x=random.randint(0,screen_width-e_w)
        e_y=0

    #2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            running=False

    #3. 게임 캐릭터 위치 정의
        if event.type==pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key==pygame.K_LEFT:
                to_x-=c_sp
            elif event.key==pygame.K_RIGHT:
                to_x+=c_sp
           
        
        if event.type==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0

    c_x +=to_x *dt
    e_y +=e_sp
    if c_x<0:
        c_x=0
    elif c_x>screen_width-c_w:
        c_x=screen_width-c_w
    
    #4. 충돌 처리
    c_r=c.get_rect()
    c_r.left=c_x
    c_r.top=c_y

    e_r=e.get_rect()
    e_r.left=e_x
    e_r.top=e_y

    if c_r.colliderect(e_r):
        running=False

    #5. 화면에 그리기
    screen.blit(bg,(0,0))
    screen.blit(c,(c_x,c_y))
    screen.blit(e,(e_x,e_y))

    pygame.display.update()

pygame.quit()

