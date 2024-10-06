import pygame
import random
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

pygame.init()
pygame.mixer.init()


pygame.mixer.music.load('menuMusic.mp3')
pygame.mixer.music.play(-1)
ow = pygame.mixer.Sound('pain sound.mp3')
munch = pygame.mixer.Sound('munch.mp3')
click = pygame.mixer.Sound('click.mp3')
lose = pygame.mixer.Sound('lose.mp3')
yay = pygame.mixer.Sound('yay.mp3')
screen = pygame.display.set_mode((1000,600))

start = True
play = False
help1 = False
help2 = False
help3 = False
creds = False
over = False

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

transparent_surface = pygame.Surface((140, 40), pygame.SRCALPHA)
transparent_surface.fill((120, 120, 120, 150))
rect_x, rect_y = 10, 70

startScreen = pygame.image.load('1.png')
playScreen = pygame.image.load('PLAY.png')
helpScreen1 = pygame.image.load('inst1.png')
helpScreen2 = pygame.image.load('inst2.png')
helpScreen3 = pygame.image.load('inst3.png')
credScreen = pygame.image.load('creds.png')
overScreen = pygame.image.load('gamover.png')
winScreen = pygame.image.load('win.png')

twins = pygame.image.load('besttwin.png')
hoverflower = pygame.image.load('besttwin.png')
hoverflower.set_alpha(128)
kitty = pygame.image.load('kitty.png')
hoverkitty = pygame.image.load('kitty.png')
hoverkitty.set_alpha(128)
melody = pygame.image.load('melody.png')
hovermelody = pygame.image.load('melody.png')
hovermelody.set_alpha(128)
purin = pygame.image.load('purin.png')
hoverpurin = pygame.image.load('purin.png')
hoverpurin  .set_alpha(128)
sam = pygame.image.load('sam.png')
hoversam = pygame.image.load('sam.png')
hoversam.set_alpha(128)
zomb = pygame.image.load('zomb.png')
pochacco = pygame.image.load('pochacco.png')
keroppi = pygame.image.load('keroppi.png')
kuromi = pygame.image.load('kuromi.png')
bossPic = pygame.image.load('boss.png')
twins1 = pygame.image.load('twins1.png')
twins2 = pygame.image.load('twins2.png')
kitty1 = pygame.image.load('kitty1.png')
kitty2 = pygame.image.load('kitty2.png')
melody1 = pygame.image.load('melody1.png')
melody2 = pygame.image.load('melody2.png')
purin1 = pygame.image.load('purin1.png')
purin2 = pygame.image.load('purin2.png')
sam1 = pygame.image.load('sam1.png')
sam2 = pygame.image.load('sam2.png')

starPic = pygame.image.load('star.png')
bow1f = pygame.image.load('bow1.png')
bow2f = pygame.image.load('bow2.png')
bow1 = pygame.transform.scale(bow1f, (40, 20))
bow2 = pygame.transform.scale(bow2f, (40, 20))
shovel = pygame.image.load('shovel.png')
shovel.set_alpha(128)

class plant:
    def __init__(self, name, price, health, shootInt, pic):
        self.name = name
        self.price = price
        self.health = health
        self.shootInt = shootInt
        self.pic = pic

class star:
    def __init__(self, x, ypos, max):
        self.x = x
        self.ypos = ypos
        self.max = max

board = [[None]*10 for _ in range(5)]
HEALTH = 3
MONEY = 0
selected = -1
sec = 0
font = pygame.font.Font(None, 56)
enemies = []
stars = []
projectiles = []

class projectile:
    def __init__(self, row, x, type):
        self.row = row
        self.x = x
        self.type = type

class enemy:
    def __init__(self, row, x, type, health, munch):
        self.row = row
        self.x = x
        self.type = type
        self.health = health 
        self.munch = munch
def rowCheck(n):
    for e in enemies:
        if e.row == n:
            return True
    return False
plants = {
    2:plant("kitty",4,10,2*60,[kitty,kitty1,kitty2]),
    1:plant("twins",2,5,5*60,[twins,twins1,twins2]),
    3:plant("melody",10,12,1*60,[melody,melody1,melody2]),
    4:plant("purin",6,8,10*60, [purin,purin1,purin2]),
    5:plant("sam",4,20,99999999999999999999*9999999999999999999,[sam,sam1,sam2])
}
enemer = {
    1:zomb,
    2:pochacco,
    3:keroppi,
    4:kuromi,
    69:bossPic
}
reverse = {
    "kitty":2,
    "twins":1,
    "melody":3,
    "purin":4,
    "sam":5
}
randomtimer = random.randint(90,3*60)
hold = 12*60
spawntimer = 20*60


hell = 0
kur = 0
poc = 0
kers = 0
boss = False
bossPhase = False
win = False

while True: 
    mouse = pygame.mouse.get_pos() 
    x = mouse[0]
    y = mouse[1]
    indx = x//100
    indy = (y//100)-1
    if play:
        sec += 1
        randomtimer-=2
        spawntimer -= 1
        if boss and len(enemies) == 0:
            enemies.append(enemy(0,985,69,400,1))
            bossPhase = True
        if kers >= 12 and not boss:
                hold = 99999999999
                pygame.mixer.music.load('bossMusic.mp3')
                pygame.mixer.music.play(-1)
                boss = True
        if spawntimer <= 0:
            if hold > 20:
                hold *= 0.91
            elif hold > 10:
                hold *= 0.98
            elif hold > 8:
                hold *= 0.995
            spawntimer = hold
            ranrow = random.randint(0,4)
            r = random.randint(1,4)
            if r == 1 or hell == 0:
                #enemies.append(enemy(0,999,69,1000,1))
                hell = 1
                enemies.append(enemy(ranrow,999,1,12,60))
            elif r == 4 or kur == 0:
                kur = 1
                enemies.append(enemy(ranrow,999,4,10,60))
            elif r == 2 or poc == 0:
                poc = 1
                enemies.append(enemy(ranrow,999,2,20,60))
            elif r == 3:
                enemies.append(enemy(ranrow,999,3,30,60))
        screen.blit(playScreen,(0,0))
        
        mony = font.render(f'{MONEY}', True, (0,0,0))
        healf = font.render(f'{HEALTH}', True, (0,0,0))
        screen.blit(healf, (840, 36))
        centerer = mony.get_rect(center=(948, 56))
        screen.blit(mony, centerer)
        if selected > -1 and indy >= 0:
            if board[indy][indx] is None:
                if selected == 1:
                    screen.blit(hoverflower,(indx*100+5,(indy+1)*100+5))
                if selected == 2:
                    screen.blit(hoverkitty,(indx*100+5,(indy+1)*100+5))
                if selected == 3:
                    screen.blit(hovermelody,(indx*100+5,(indy+1)*100+5))
                if selected == 4:
                    screen.blit(hoverpurin,(indx*100+5,(indy+1)*100+5))
                if selected == 5:
                    screen.blit(hoversam,(indx*100+5,(indy+1)*100+5))
        for i in range(5):
            for j in range(10):
                guy = board[i][j]
                if guy is not None:
                    screen.blit(guy.pic[2-int((guy.health/plants[reverse[guy.name]].health)/0.35)],(j*100+5,(i+1)*100+5))
                    guy.shootInt -= 1
                    if guy.name == "purin":
                        h = int((guy.shootInt/(10*60))*25)
                        rect2 = pygame.Rect(j*100+75, (i+1)*100, 25, 25)
                        pygame.draw.rect(screen, (255,0,0), rect2)
                        rect = pygame.Rect(j*100+75, (i+1)*100, 25, h)
                        pygame.draw.rect(screen, (0,0,0), rect)
                        
                    if guy.shootInt < 0:
                        if guy.name != "purin":
                            guy.shootInt = plants[reverse[guy.name]].shootInt
                        if guy.name == "twins":
                            stars.append(star(j*100+35,(i+1)*100+50,(i+1)*100+50))
                        elif guy.name == "purin":
                            for k in range(len(enemies)):
                                if j*100+205>=enemies[k].x>=j*100 and i == enemies[k].row:
                                    enemies.pop(k)
                                    guy.shootInt = plants[reverse[guy.name]].shootInt
                                    #munch.play
                                    break
                        elif rowCheck(i) or bossPhase:
                            if guy.name == "kitty":
                                projectiles.append(projectile(i,j*100+40,1))
                            elif guy.name == "melody":
                                projectiles.append(projectile(i,j*100+40,2))
                        

        for i in range(len(projectiles)-1,-1,-1):
            if win:
                break
            pro = projectiles[i]
            im = None
            if pro.type == 1:
                im = bow1
            else:
                im = bow2
            screen.blit(im,(pro.x,pro.row*100+140))
            if pro.x < 1080:
                pro.x+=4
                for j in range(len(enemies)-1,-1,-1):
                    if (enemies[j].row == pro.row or enemies[j].type == 69) and enemies[j].x+20>pro.x>enemies[j].x:
                        enemies[j].health -= 2
                        projectiles.pop(i)
                        if enemies[j].health <= 0:
                            if enemies[j].type == 4:
                                kers += 1
                            if enemies[j].type == 69:
                                win = True
                                play = False
                            enemies.pop(j)
                        break
            else:
                projectiles.pop(i)
        if win:
            play = False
            screen.blit(winScreen,(0,0))
            pygame.mixer.music.stop()
            yay.play()

        for i in range(len(enemies)-1,-1,-1):
            en = enemies[i]
            im = enemer[en.type]
            p = board[en.row][int(en.x//100)]
            if en.type == 69:
                en.x-=0.5
                for i in range(5):
                    board[i][int(en.x//100)] = None
            elif p is not None:
                if en.munch == 60:
                    munch.play()
                en.munch-=1
                if en.munch <= 0:
                    en.munch = 60
                    p.health -= 1
                    if p.health <= 0:
                        board[en.row][int(en.x//100)] = None
            else:
                if en.type == 1:
                    en.x-=1.5
                elif en.type == 2:
                    en.x-=0.75
                elif en.type == 3:
                    en.x-=0.5
                elif en.type == 4:
                    en.x-=2
                else:
                    en.x-=0.75
            screen.blit(im,(en.x,en.row*100+105))
            if en.x < 0:
                HEALTH-=1
                if en.type == 69:
                    HEALTH = 0
                if HEALTH != 0:
                    ow.play()
                enemies.pop(i)
                if HEALTH <= 0:
                    break
        if 90 >= x >= 10 and 90 >= y >= 10:
            c = "Cost: 2"
            cr = font.render(c, True, (255,255,255))
            rect_x, rect_y = 10, 70
            screen.blit(transparent_surface, (rect_x, rect_y))
            tr = cr.get_rect(center=(rect_x + 140 / 2, rect_y + 40 / 2))
            screen.blit(cr, tr)
        elif 190 >= x >= 110 and 90 >= y >= 10:
            c = "Cost: 4"
            cr = font.render(c, True, (255,255,255))
            rect_x, rect_y = 80, 70
            screen.blit(transparent_surface, (rect_x, rect_y))
            tr = cr.get_rect(center=(rect_x + 140 / 2, rect_y + 40 / 2))
            screen.blit(cr, tr)
        elif 290 >= x >= 210 and 90 >= y >= 10:
            c = "Cost: 10"
            cr = font.render(c, True, (255,255,255))
            rect_x, rect_y = 180, 70
            screen.blit(transparent_surface, (rect_x, rect_y))
            tr = cr.get_rect(center=(rect_x + 140 / 2, rect_y + 40 / 2))
            screen.blit(cr, tr)
        elif 390 >= x >= 310 and 90 >= y >= 10:
            c = "Cost: 6"
            cr = font.render(c, True, (255,255,255))
            rect_x, rect_y = 280, 70
            screen.blit(transparent_surface, (rect_x, rect_y))
            tr = cr.get_rect(center=(rect_x + 140 / 2, rect_y + 40 / 2))
            screen.blit(cr, tr)
        elif 490 >= x >= 410 and 90 >= y >= 10:
            c = "Cost: 4"
            cr = font.render(c, True, (255,255,255))
            rect_x, rect_y = 380, 70
            screen.blit(transparent_surface, (rect_x, rect_y))
            tr = cr.get_rect(center=(rect_x + 140 / 2, rect_y + 40 / 2))
            screen.blit(cr, tr)

        if HEALTH <= 0:
            play = False
            healf = font.render(f'{HEALTH}', True, (0,0,0))
            pygame.draw.circle(screen, (198,48,44), (850, 50), 20)
            screen.blit(healf, (840, 36))
            screen.blit(overScreen,(0,0))
            pygame.mixer.music.stop()
            lose.play()

            over = True
        elif not win:
            for ent in stars:
                screen.blit(starPic,(ent.x,ent.ypos))
                if ent.ypos < ent.max:
                    ent.ypos+=3
            if randomtimer < 0:
                randomtimer = random.randint(10*60,12*60)
                stars.append(star(random.randint(200,840),90,random.randint(140,480)))
            if selected == -2:
                screen.blit(shovel,(x,y))
    elif start:
        screen.blit(startScreen,(0,0))
    elif help1:
        screen.blit(helpScreen1,(0,0))
    elif help2:
        screen.blit(helpScreen2,(0,0))
    elif help3:
        screen.blit(helpScreen3,(0,0))
    elif creds:
        screen.blit(credScreen,(0,0))
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if start and 620>x>360 and 390>y>330:
                start = False
                play = True
                pygame.mixer.music.load('fightMusic.mp3')
                pygame.mixer.music.play(-1)
            elif start and x>360 and x<620 and y > 405 and y < 465:
                start = False
                help1 = True
            elif start and 110>x>10 and 585>y>560:
                start = False
                creds = True
            elif help1 and 585<x<705 and 445<y<490:
                help1 = False
                start = True
            elif help1 and 720<x<840 and 445<y<490:
                help1 = False
                help2 = True
            elif help2 and 585<x<705 and 445<y<490:
                help2 = False
                help1 = True
            elif help2 and 720<x<840 and 445<y<490:
                help2 = False
                help3 = True
            elif help3 and 585<x<705 and 445<y<490:
                help3 = False
                help2 = True
            elif help3 and 720<x<840 and 445<y<490:
                help3 = False
                start = True
            elif creds and 135 >= x >= 15 and 587 >=y>=542:
                creds= False
                start = True
            elif (win or over) and 380<=x<=620 and 400<=y<=462:
                hold = 12*60
                spawntimer = 20*60
                enemies = []
                stars = []
                projectiles = []
                board = [[None]*10 for _ in range(5)]
                HEALTH = 3
                MONEY = 0
                selected = -1
                play = True
                over = False
                win = False
                boss = False
                bossPhase = False
                hell = 0
                kur = 0
                poc = 0
                kers = 0
                pygame.mixer.music.load('fightMusic.mp3')
                pygame.mixer.music.play(-1)
            elif (win or over) and 380<=x<=620 and 480<=y<=540:
                hold = 12*60
                spawntimer = 20*60
                enemies = []
                stars = []
                projectiles = []
                board = [[None]*10 for _ in range(5)]
                HEALTH = 3
                MONEY = 0
                selected = -1
                start = True
                over = False
                win = False
                boss = False
                bossPhase = False
                hell = 0
                kur = 0
                poc = 0
                kers = 0
                pygame.mixer.music.load('menuMusic.mp3')
                pygame.mixer.music.play(-1)
            elif play:
                for i in range(len(stars)):
                    fallen = stars[i]
                    if fallen.x+50>=x>=fallen.x and fallen.ypos+50>=y>=fallen.ypos:
                        MONEY+=1
                        #ADD STAR ANIMATION
                        stars.pop(i)
                        break
                if 710 <= x <= 785 and 85 >= y >= 15:
                    if selected == -2:
                        selected = -1
                    else:
                        selected = -2
                elif 90 >= x >= 10 and 90 >= y >= 10:
                    if selected == 1:
                        selected = -1
                    else:
                        selected = 1
                elif 190 >= x >= 110 and 90 >= y >= 10:
                    if selected == 2:
                        selected = -1
                    else:
                        selected = 2
                elif 290 >= x >= 210 and 90 >= y >= 10:
                    if selected == 3:
                        selected = -1
                    else:
                        selected = 3
                elif 390 >= x >= 310 and 90 >= y >= 10:
                    if selected == 4:
                        selected = -1
                    else:
                        selected = 4
                elif 490 >= x >= 410 and 90 >= y >= 10:
                    if selected == 5:
                        selected = -1
                    else:
                        selected = 5
                elif selected > -1 and y >= 100 and board[indy][indx] is None and plants[selected].price <= MONEY:
                    board[indy][indx] = plant(plants[selected].name,plants[selected].price,plants[selected].health,plants[selected].shootInt//4,plants[selected].pic)
                    MONEY-=plants[selected].price
                    selected = -1
                elif selected == -2 and board[indy][indx] is not None:
                    selected = -1
                    board[indy][indx] = None
    pygame.display.update() 
    pygame.time.Clock().tick(60)