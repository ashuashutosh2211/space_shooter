import pygame 
import random
import math 
pygame.init() 
# create screen 
screen = pygame.display.set_mode((800,600))

#background image 
backgnd = pygame.image.load("bg.png") 


#title and icon 
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("arcade-game.png")
pygame.display.set_icon(icon)

#Player / shooter
playerimage = pygame.image.load("space-invaders.png") 
playerX = 370 
playerY = 500
changeXplayer = 0
changeYplayer = 0 
def player(x,y):
    screen.blit(playerimage,(x,y)) 
#enemy
enemyimage = []
enemyX = []
enemyY = []
changeXenemy = []
changeYenemy = []
n = 6 
for i in range(n):

    enemyimage.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    changeXenemy.append(3)
    changeYenemy.append(40)
def enemy(x,y,i):
    screen.blit(enemyimage[i],(x,y)) 

#bullet 
bulletimage = pygame.image.load("bullet.png") 
bulletX = 0 
bulletY = 480
bulletX_change = 0 
bulletY_change = 10
bullet_state = "ready" 

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletimage,(x+16,y+10))

#collision detection 
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((enemyX -bulletX)**2 + (enemyY - bulletY)**2)
    if(distance <27):
        return True 
    return False 
#SCORE
score = 0 
font = pygame.font.Font("freesansbold.ttf",32) 
textX = 10 
textY = 10 
def showscore(x,y):
    scr = font.render("Score " + str(score),True , (255,255,255)) 
    screen.blit(scr,(x,y))     

def gameover(x,y):
    gmovr = pygame.font.Font("freesansbold.ttf",44)
    h = gmovr.render("GAME OVER",True, (255,255,255)) 
    screen.blit(h,(x,y))  

# GAME LOOP
running = True
a = 0 
while running:
    #RGB color 
    screen.fill((14, 67, 82))
    screen.blit(backgnd,(0,0))
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running = False 
        # if keys are pressed 
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                changeXplayer = -5
            if(event.key == pygame.K_RIGHT):
                changeXplayer = 5
            if(event.key == pygame.K_SPACE):
                if(bullet_state == "ready"):
                    bulletX =  playerX
                    fire_bullet(bulletX,bulletY) 
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                changeXplayer = 0 
    playerX += changeXplayer 
    if(playerX<=0):
        playerX = 0 
    elif playerX >=736:
        playerX = 736
    for i in range(n):
        if(enemyY[i]>=440):
            for j in range(n):
                enemyY[j] = 1000
            gameover(300,250)
            break
        enemyX[i] += changeXenemy[i]
        if(enemyX[i] <=0):
            changeXenemy[i] = 3
            enemyY[i] += changeYenemy[i]
            
        elif enemyX[i]>=736:
            changeXenemy[i] = -3
            enemyY[i] += changeYenemy[i]
            
    #check for collision between enemy and bullet 
        if(isCollision(enemyX[i],enemyY[i],bulletX,bulletY)):
            bulletY = 480 
            bullet_state = "ready"
            score += 1 
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    
    if(bulletY<=0):
        bulletY = 480 
        bullet_state = "ready"
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    
    
    player(playerX,playerY)
    showscore(textX,textY)
    pygame.display.update() 
