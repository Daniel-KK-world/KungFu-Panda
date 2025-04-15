import pygame 

pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

#setting a background
background_img = pygame.image.load('bg\dfqdssy-e24be69d-bdc3-4c49-8dc6-a1675168f19e.png')
background_img = pygame.transform.scale(background_img, (900, 600))  # Scale to screen size
 
# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
 
# Basic parameters of the screen
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
# Used to adjust the frame rate
clock = pygame.time.Clock()
FPS = 30

#my sticks 
class Sticks:
    def __init__(self, x, y, width=20, height=600):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (152, 251, 152) # pale green 
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

sticks = [
    Sticks(100, 0),
    Sticks(200, 0),  # y is 0 to start at top
    Sticks(300, 0),
    Sticks(400, 0),
    Sticks(500, 0),
    Sticks(600, 0)
]

# Main game loop
running = True 
while running:
    # Handle events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # Draw background first
    screen.blit(background_img, (0, 0))
    
    # Draw all sticks
    for stick in sticks:
        stick.draw(screen)

    # Update display
    pygame.display.flip()
    
    # Stable frame rate
    clock.tick(FPS)  # Use the FPS constant you defined
    
pygame.quit()