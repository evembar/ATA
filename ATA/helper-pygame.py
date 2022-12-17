import os
import time

work = True

print('Пожалуйста подождите...')
time.sleep(3)
print('Добро пожаловать в помощник pygame')
time.sleep(3)
while work:
    com = input("Что вас интересует?(Например: скелет, фон, музыка) ")
    if com == 'скелет':
        speedp = input('Укажите скорость для объектов> ')
        namep = input('Укажите название программы> ')
        widthp = input('Укажите ширину окна> ')
        heigtp = input('Укажите высоту окна> ')
        print(f'\nimport pygame\nimport random\n\nWIDTH = {widthp}\nHEIGHT = {heigtp}\nFPS = 30\nspeed = {speedp}\nx = 50\n y = 50\n\npygame.init()\npygame.mixer.init()\nscreen = pygame.display.set_mode((WIDTH, HEIGHT))')
        print(f'pygame.display.set_caption("{namep}")\nclock = pygame.time.Clock()\n\nrunning = True\nwhile running:\n    clock.tick(FPS)\n    for event in pygame.event.get():')
        print('        if event.type == pygame.QUIT:\n            running = False\n    pygame.display.update()\n    pygame.quit()\n')
    elif com == 'фон':
        bckg = input('Напишите название изображения (Учтите, что имеется про тот каталог,где запущен этот скрипт)> ')
        y = input('Введите координату по Y> ')
        x = input('Введите координату по X> ')
        print(f'\nfilename = "{bckg}"\nmyImage = pygame.image.load(filename)\nmyRect = {x},{y}\nscreen.blit(myImage,myRect)\n')
    elif com == 'музыка':
        funp = input('Остановить или проиграть? ')
        if funp == 'Остановить' or funp == 'остановить':
               musp = input('Введите название музыки> ')
               print(f'\npygame.mixer.music.stop()\n')
        elif funp == 'Проиграть' or funp == 'проиграть':
               musp = input('Введите название музыки> ')
               loops = input('Сколько раз повторять музыку> ')
               print(f'\npygame.mixer.music.load("{musp}")\npygame.miser.music.play(loops = {loops}, -1)\n')
    elif com == 'управление':
        keyp = input('Какое управление подходит вам:\nwasd\nстрелочки\n> ')
        if keyp == 1 or keyp == 'wasd':
            print('\n    keys = pygame.key.get_pressed()\n\n    if keys[pygame.A]:\n        x-= speed\n    elif keys[pygame.D]:')
            print('        x += speed\n    elif keys[pygame.S]:\n      y-= speed\n    elif keys[pygame.W]:\n        y += speed\n')
        elif keyp == 'стрелочки':
            print('\n    keys = pygame.key.get_pressed()\n\n    if keys[pygame.K_LEFT]:\n        x-= speed\n    elif keys[pygame.K_RIGHT]:')
            print('        x += speed\n    elif keys[pygame.K_UP]:\n      y-= speed\n    elif keys[pygame.K_DOWN]:\n        y += speed\n')

