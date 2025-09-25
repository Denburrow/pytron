import pygame
import sys
import asyncio
import threading
import time

pygame.init()

running = False
play = True

FPS = 60
x = 50
y = 50
x2 = 590
y2 = 50
width = 640
height = 480
dire = 'right'
dire2 = 'left'
speed = 200
speed2 = 200

right = False

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pyTRON')
clock = pygame.time.Clock()
clock.tick(FPS)

trail = []
trail2 = []
position_buffer = []
position_buffer2 = []
BUFFER = 2

while play:

    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if dire == 'down':
                dire == 'down'
            else:
                if event.key == pygame.K_w:
                    dire = 'up'

                    collide = False
            if dire == 'up':
                dire == 'up'
            else:
                if event.key == pygame.K_s:
                    dire = 'down'

                    collide = False
            if dire == 'left':
                dire = 'left'
            else:
                if event.key == pygame.K_d:
                    dire = 'right'

                    collide = False
            if dire == 'right':
                dire = 'right'
            else:
                if event.key == pygame.K_a:
                    dire = 'left'
            if event.key == pygame.K_q:
                speed = 300
            else:
                speed = 200
        if event.type == pygame.KEYDOWN:
            if dire2 == 'down':
                dire2 == 'down'
            else:
                if event.key == pygame.K_UP:
                    dire2 = 'up'

                    collide = False
            if dire2 == 'up':
                dire2 == 'up'
            else:
                if event.key == pygame.K_DOWN:
                    dire2 = 'down'

                    collide = False
            if dire2 == 'left':
                dire2 = 'left'
            else:
                if event.key == pygame.K_RIGHT:
                    dire2 = 'right'

                    collide = False
            if dire2 == 'right':
                dire2 = 'right'
            else:
                if event.key == pygame.K_LEFT:
                    dire2 = 'left'
            if event.key == pygame.K_RETURN:
                speed2 = 300
            else:
                speed2 = 200


    if event.type == pygame.QUIT:
        running = False

    if dire == 'right':
        x += speed * dt
            #trail.append(player.copy())
    elif dire == 'down':
        y += speed * dt
            #trail.append(player.copy())
    elif dire == 'up':
        y -= speed * dt
            #trail.append(player.copy())
    elif dire == 'left':
        x -= speed * dt
            #trail.append(player.copy())

    if dire2 == 'right':
        x2 += speed2 * dt
            #trail.append(player.copy())
    elif dire2 == 'down':
        y2 += speed2 * dt
            #trail.append(player.copy())
    elif dire2 == 'up':
        y2 -= speed2 * dt
            #trail.append(player.copy())
    elif dire2 == 'left':
        x2 -= speed2 * dt
            #trail.append(player.copy())

    screen.fill((0, 0, 0))

    player = pygame.draw.rect(screen, (0,0,255), (x, y, 5, 5))

    player2 = pygame.draw.rect(screen, (255,0,0), (x2, y2, 5, 5))

        #print(x, y)

    position_buffer.append(player.copy())
    if len(position_buffer) > BUFFER:
        trail.append(position_buffer.pop(0))

    for segment in trail:
        pygame.draw.rect(screen, (0, 0, 255), segment)

    for segment in trail[:-BUFFER]:
        if player.colliderect(segment):
            play = False
            print('p2 wins')
        if player2.colliderect(segment):
            play = False
            print('p1 wins')
    position_buffer2.append(player2.copy())
    if len(position_buffer2) > BUFFER:
        trail2.append(position_buffer2.pop(0))

    for segment in trail2:
        pygame.draw.rect(screen, (255, 0, 0), segment)

    for segment in trail2[:-BUFFER]:
        if player2.colliderect(segment):
            play = False
            print('p1 wins')
        if player.colliderect(segment):
            play = False
            print('p2 wins')

    if x > width:
        play = False
        print('p2 wins')
    if x < 0:
        play = False
        print('p2 wins')
    if y > height:
        play = False
        print('p2 wins')
    if y < 0:
        play = False
        print('p2 wins')
    if x2 > width:
        play = False
        print('p1 wins')
    if x2 < 0:
        play = False
        print('p1 wins')
    if y2 > height:
        play = False
        print('p1 wins')
    if y2 < 0:
        play = False
        print('p1 wins')

    pygame.display.flip()

pygame.quit()
