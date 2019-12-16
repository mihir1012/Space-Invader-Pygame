import  pygame,sys,random,math
from pygame import mixer
import enemyLoc
#intialize the py game (Compulsory)
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon and Background
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Space ICon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('SpaceBackground.jpg')

#Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

#Player
PlayerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_Change = 0

def player():
    screen.blit(PlayerImg,(playerX,playerY))

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
numEnemy =6
for i in range(numEnemy):
    enemyImg.append(pygame.image.load('monster.png'))
    enemyX_Change.append(2.5)
    enemyY_Change.append(30)
def enemy():
    for i in range(numEnemy):
        screen.blit(enemyImg[i],(enemyX[i],enemyY[i]))
(enemyX,enemyY)=enemyLoc.enemyRoute(numEnemy,enemyX_Change[0],enemyY_Change[0])
#Gameover Text
Gameoverfont = pygame.font.Font('freesansbold.ttf',64)
GameovertextX = 200
GameovertextY = 250
def gameover():
    gameovertext = Gameoverfont.render("GAME OVER!!!",True,(255,0,0))
    screen.blit(gameovertext,(GameovertextX,GameovertextY))
    
#score
collisionSound = mixer.Sound('explosion.wav')    
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def showScore():
    score_value = font.render("Score:" + str(score),True,(255,255,255))
    screen.blit(score_value,(textX,textY))

#Bullet
BulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"
bulletSound = mixer.Sound('laser.wav')
def fireBullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(BulletImg , ( x + 16, y + 10))
def isCollision(enemycolX,enemycolY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemycolX-bulletX,2)+math.pow(enemycolY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False

#GameLoop
while 1:
    screen.fill((125,25,125))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit clicked")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bulletSound.play()
                bulletX = playerX
                fireBullet(bulletX , bulletY)
            if event.key == pygame.K_RIGHT:
                playerX_Change = 5
            if event.key == pygame.K_LEFT:
                playerX_Change =-5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_Change = 0
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player()
    #enemyMovement
    for i in range(numEnemy):
        #GameOVER
        if enemyY[i] < 1000 and enemyY[i] > 440:
            print(enemyY[i])
            for j in range(numEnemy):
                enemyY[j] = 2000
            gameover()
            break
        enemyX[i] += enemyX_Change[i] 
        if enemyX[i] <= 0:
            enemyX_Change[i] = 2.5
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 736:
            enemyX_Change[i] = -2.5
            enemyY[i] += enemyY_Change[i]
        if enemyY[i] >= 536:
            enemyY_Change[i] = -30
            enemyY[i] +=enemyY_Change[i]
        elif enemyY[i] <= 0:
            enemyY_Change[i] = 30
            enemyY[i] +=enemyY_Change[i]
    enemy()
    
    #bullet Fire
    if bullet_state is "fire":
        fireBullet(bulletX,bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = playerY
            bullet_state ="ready"
    #collision
    for i in range(numEnemy):
        if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY = playerY
            bullet_state = "ready"
            collisionSound.play()
            score += 1
            enemyY[i]=-1000
            if (score % numEnemy) == 0:
                (enemyX,enemyY) = enemyLoc.enemyRoute(numEnemy,enemyX_Change[0],enemyY_Change[0])
                print("Called")
    showScore()
    pygame.display.update()
