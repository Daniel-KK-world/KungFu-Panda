import pygame 

pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)
 
# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
 
# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
# Used to adjust the frame rate
clock = pygame.time.Clock()
FPS = 30

#main game loop
running = True 
while running:
    #Handle events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #To well update game objects 

    #Draw my stuff like the sticks blah blah 
    screen.fill((0, 0, 0))
    pygame.display.flip()
    
    #stable frame rate
    clock.tick(60) 
    
#now ideally we'd quit too 
pygame.quit()