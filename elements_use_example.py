import keyboard
import pygame

#Load all our elements
from data.classes.constructor.Elements import *
# Set screen
screen_scale = 1.5
w, h = int(1200 * screen_scale), int(600 * screen_scale)
screen_size = [w, h]
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Just caption')
screen_info = [screen, screen_scale, screen_size]

# To control fps
clock = pygame.time.Clock()

running = True

pygame.init()
from data.classes.MainMenu import Menu

menu = Menu(screen_info)


# create an image object with 0.4 scale
myImg = Img(screen_info, 'data/images/heroes/bercerk_hero.png', k=0.4)

# create a Card. 2-nd parameter you can find in /data/global_vars/deck ... cards variable (keys of this dictionary)
#we use index to understand what card is focused right now (another cards must 'move over')
myCard1 = Card(screen_info, 'attack', 0.5, 0)
#try set 0 index to card and check card behaviour
myCard2 = Card(screen_info, 'defense', 0.5, 1)

#Create text object and set optional parameters
myText = Text('The carder',k=0.8, color=[200,200,255])
#Why I also use CText? Text use mainMenu text font by default, CText uses arial font by default
myCText = CText('The carder', k=0.8, color=[200,200,255])

#crete 2 buttons:
text_info = ['Click me!', 0.8, (100,100,100)]
myTextButton = TextButton(text_info, (1200, 200),  screen, 0)
src = 'data/images/elements/buttons/next_turn.png','data/images/elements/buttons/next_turn_light.png'
myImgButton = ImgButton(screen_info, src, (1200, 400), k=0.2)

#create
#hero
hero_class = 'bercerk'

while running:
    #fill all by black, without background you'll see strange classes behaviour
    screen.fill([0,0,0])

    #place my Img object on the half of the screen
    myImg.draw(screen, (w//2-myImg.get_width()//2,h//2-myImg.get_height()//2))
    
    #place a CardImg object right up
    myCard1.live(screen, (1200,h-myCard1.get_height()))
    myCard2.live(screen, (1200+myCard1.get_width(), h - myCard2.get_height()))
    
    #place texts
    myText.draw(screen, (100,200))
    myCText.draw(screen, (100, 400))
    
    #place buttons
    if myTextButton.draw_check_click(): print('CLICKED TEXT BUTTON!')
    if myImgButton.draw_check_click(): print('CLICKED IMG BUTTON!')
    
    
    # Updating display, control fps
    pygame.display.update()
    clock.tick(60)

    #you can use q (or alt+f4 of courseq) to quit, but sometimes you'll see memory error. I don`t know why
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if keyboard.is_pressed('q'):
        running = False

print('OK!')