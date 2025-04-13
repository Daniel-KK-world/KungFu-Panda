import pygame 

pygame.init()

#display setup 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kung Fu Panda")

#clock for fps
clock = pygame.time.Clock()

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