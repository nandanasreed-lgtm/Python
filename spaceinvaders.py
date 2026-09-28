import math
import random
import pygame

screen_height = 500
screen_width = 800
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 1
enemy_speed_y = 10
bullet_speed_y = 10
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.transform.scale(pygame.image.load("background.jpg").convert(),(screen_width, screen_height))

pygame.display.set_caption("SPACE INVADERS")

icon = pygame.image.load("player.png")
pygame.display.set_icon(icon)

playerIng = pygame.transform.scale(pygame.image.load("player.png").convert_alpha(), (64, 64))
playerX = player_start_x
playerY = player_start_y
playerX_change = 0

enemyIng = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
for i in range(5):
    enemyIng.append(pygame.transform.scale(pygame.image.load("enemy.png").convert_alpha(),(64, 64)))
    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)

bulletIng = pygame.image.load("bullet.png")
bulletX = 0
bulletY = player_start_y
bulletX_change = 0
bulletY_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

overfont = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def gameover_text():
    overtext = overfont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overtext, (200, 250))

def player(x, y):
    screen.blit(playerIng, (x, y))

def enemy(x, y, i):
    screen.blit(enemyIng[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIng, (x + 16, y + 10))

def is_colllision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)** 2 + (enemy_y - bullet_y)** 2)
    return distance < collision_distance

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
    playerX += playerX_change
    playerX = max(0, min(playerX, screen_width - 64))
    for i in range(5):
        if enemyY[i] > 340:
            for j in range(5):
                enemyY[j] = 2000
            gameover_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= screen_width - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        if is_colllision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, screen_width - 64)
            enemyY[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
        enemy(enemyX[i], enemyY[i], i)
    if bulletY <= 0:
        bulletY = player_start_y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
    
