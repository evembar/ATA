import pygame
import sys
import time
def script(color_metro,
           metro_font):
 global butevent
 pygame.init()
 pygame.mixer.init()
 pygame.font.init()
 clock = pygame.time.Clock()
 screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
 close_button = [pygame.image.load('images/metro_icon/close/close-actived.png'),
                   pygame.image.load('images/metro_icon/close/close-no_active.png')]
 ask = False
 butevent = False
 xbut = 0
 ybut = 0
 def metro_ui():
     screen.fill(color_metro[1])
     pygame.draw.rect(screen, (color_metro[0]), 
                 (0, 0, 10000, 100))
     metro_hide_name = pygame.font.Font(metro_font[1], 36)
     metro_text = metro_hide_name.render('ATA Framework example', True,
                                         color_metro[1])
     screen.blit(metro_text, (30,20))
 def metro_close():
   global ask
   mouse_status = pygame.mouse.get_pressed()
   #print(mouse_status) 
   if mouse_status == (True, False, False):
     if x > 1339 and y < 30 :
        if ask == True:
            screen.blit(close_button[1], (1339, 1))
            pygame.display.flip()
            time.sleep(0.05)
            sys.exit()
   else:
     pass
 def create_metro_button(imagebutton, image, width, height, text, size, xbut, ybut, command):
  global butevent
  mouse_status = pygame.mouse.get_pressed()
  if imagebutton == True:
   pygame.image.load(image)
   screen.blit(image, (xbut,ybut))
  elif imagebutton == False and image == None or image == False or image == 0:
   pygame.draw.rect(screen, (220, 220, 220), (xbut, ybut, width, height))
   font_render = pygame.font.Font(metro_font[2], size)
   font_text = font_render.render(text, True, (0,0,0))
   screen.blit(font_text, (xbut,ybut))
  if mouse_status == (True, False, False):
   if x < xbut + width and x > xbut - width and y < ybut + height and y > ybut - height:
       butevent = (xbut, ybut)
       pygame.draw.rect(screen, (0,0,0), (xbut, ybut, width, height))
       font_text = font_render.render(text, True, (255,255,255))
       screen.blit(font_text, (xbut,ybut))
       print(ybut, xbut)
  else:
    butevent = False
 def create_metro_list_button():
    pass
 def hig():
    global butevent
    if butevent == (500, 500):
     print('ATA11')
    elif butevent == False:
     pass
 def gh():
  global butevent
  if butevent == (250, 250):
    print('55k5,5')
  elif butevent == False:
    pass
 def ask_bar():
    global ask
    if y < 5:
     pygame.draw.rect(screen, (color_metro[2]), 
                      (0, 0, 10000, 27))
     screen.blit(close_button[0], (1339, 1))
     ask_bar_name = pygame.font.Font(metro_font[1], 18)
     ask_bar_text = ask_bar_name.render('ATA Framework example', True,
                                         color_metro[1])
     screen.blit(ask_bar_text, (560,0))
     ask = True
    else:
        ask = False
 while True:
     clock.tick(30)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                 sys.exit()
         pos = pygame.mouse.get_pos()
         x,y = pos
         #print(x , y)
     create_metro_button(imagebutton = False, image = 0, width = 100, height = 30,
                          text = 'click', size = 22, xbut = 500, ybut = 500, command = hig())
     create_metro_button(imagebutton = False, image = 0, width = 100, height = 30,
                          text = 'button', size = 22, xbut = 250, ybut = 250, command = gh())
     pygame.display.flip()
     metro_ui()
     metro_close()
     ask_bar()
     
 pygame.quit()
