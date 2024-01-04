print("Hello World")            #Что-бы работало/For working
import pygame
import random

pygame.init()
width = 1366
height = 768
fps = 60

game_score = 0

game_name = "Roboid"          

screen = pygame.display.set_mode((width, height))

def draw_text(screen, text, size, x, y, color):                     #Вывод изменяемого текста на экран/Displaying editable text on the screen
    font_name = pygame.font.match_font('algerian')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_image, text_rect)

pygame.display.set_caption(game_name)

RED = '#FF0000'
WHITE = '#ffffff'
secret = str(input("Какой звук использовать Труба или Пинг: "))
if secret == "Пинг":   
    ping = pygame.mixer.Sound('ping.mp3')
elif secret == "Pipe":
    ping = pygame.mixer.Sound('Truba.mp3')
elif secret == '2444666668888888':                  #Чит код "один два три четыре пять шесть семь восемь"/Cheat code "one two three four five six seven eight"
    ping = pygame.mixer.Sound('ping.mp3')
    game_score = 10000
else:
    ping = pygame.mixer.Sound('ping.mp3')

pygame.mixer.music.load('bg.mp3')   #Прочитай txt файл/ Read the txt file
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)     #-1 --- бесконечное проигрование/-1 --- endless sound

loose = pygame.mixer.Sound('loose.mp3')


timer = pygame.time.Clock()
run = True

pic_surf = pygame.image.load('dvd.png')                         #Загрузка спрайтов/Loading sprites
pic_rect = pic_surf.get_rect()
pic_surf.set_colorkey((255, 255, 255))

racket_surf = pygame.image.load('racket.png')
racket_rect = racket_surf.get_rect()
racket_surf.set_colorkey((255, 255, 255))

drevo = pygame.image.load('drevo.png').convert()
drevo_rect = drevo.get_rect()
scale = pygame.transform.scale(drevo, (width, height))
scale_rect = scale.get_rect()


speedX = 10
speedY = 10

speedRX = 10

game_rounds = 3

racket_rect.x = width / 2 - racket_surf.get_width()/2
racket_rect.y = height - 155

while run:                  #рендер/rendering
    timer.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        racket_rect.x -=speedRX
    if key[pygame.K_RIGHT]:
        racket_rect.x +=speedRX
    
    
    screen.blit(scale, scale_rect)                                          #Размещение текста и спрайтов на экране/Placing text and sprites on the screen
    screen.blit(pic_surf, pic_rect)
    screen.blit(racket_surf, racket_rect)
    draw_text(screen, "Round " + str(game_rounds), 30, width//2, 30, RED)
    draw_text(screen, "Score " + str(game_score), 30, width//2, 65, RED)
    pic_rect.x += speedX
    pic_rect.y += speedY
    if pic_rect.bottom > height:
        pass
    
    if pic_rect.top > height:
        game_rounds -=1
        loose.play()
        pic_rect.y = 0
        pic_rect.x = random.randint(0, width)
        
        if game_rounds == 0:
            run = False
            print('Game Over')
            
    
    if pic_rect.top < 0:
        speedY = -speedY
        ping.play()
        
    if pic_rect.left < 0:
        speedX = -speedX
        ping.play()
        
    if pic_rect.right > width:
        speedX = -speedX
        ping.play()
    if pic_rect.colliderect(racket_rect):
        speedY = -speedY
        ping.play()
        game_score += 1
        speedX -= 2
        speedY -= 2
    
    
    

    pygame.display.update()
    
pygame.quit()