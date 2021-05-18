import pygame
from pathlib import Path
from mymissile import MyMissile
from player import Player
from enemy import Enemy

parent_path = Path(__file__).parents[1]
image_path = parent_path / 'res'
icon_path = image_path / 'airplaneicon.png'
pygame.display.set_caption("1942偽")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

pygame.init()
screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((50, 50, 50))
running = True
fps = 60
movingScale = 600 / fps
player = Player(playground=playground, sensitivity=movingScale)
launchMissile = pygame.USEREVENT + 1
createEnemy = pygame.USEREVENT + 2
explosion = pygame.USEREVENT + 3

Missile = []
Enemies[]
pygame.time.set_timer(createEnemy, 1000)
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == launchMissile:
            m_x = player.xy[0] + 20
            m_y = player.xy[1]
            Missile.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
            m_x = player.xy[0] + 80
            Missile.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))

        if event.type == createEnemy:
            Enemies.appendZ(Enemy(playground=playground, sensitivity=movingScale))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.to_the_left()
            if event.key == pygame.K_d:
                player.to_the_right()
            if event.key == pygame.K_s:
                player.to_the_bottom()
            if event.key == pygame.K_w:
                player.to_the_top()
            if event.key == pygame.K_SPACE:
                m_x = player.x + 20
                m_y = player.y
                Missile.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player.x + 80
                Missile.append(MyMissile(playground, (m_x, m_y), movingScale))
                pygame.time.set_timer(launchMissile, 400)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.stop_x()
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player.stop_y()
            if event.key == pygame.K_SPACE:
                pygame.time.set_timer(launchMissile, 0)

    screen.blit(background, (0, 0))
    player.collided_detect(Enemies)
    for e in Enemies:
        if e.collided:
            Boom.append(Explosion(e.center))

    Missile = [item for item in Missile if item.available]
    for m in Missile:
        m.update()
        screen.blit(m.image, m.xy)
    Enemies = [item for item in Enemies if item.available]
    for e in Enemies:
        e.update()
        screen.blit(e.image, e.xy)
    player.update()
    screen.blit(player.image, player.xy)
    Boom = [item for item in Boom if item.available]
    for e in Boom:
        e.update()
    pygame.display.update()
    dt = clock.tick(fps)
pygame.quit()
