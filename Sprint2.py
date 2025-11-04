Sprint 2
import pygame
import random as rand
pygame.init()


Screen_Width = 750
Screen_Height = 750
screen = pygame.display.set_mode ((Screen_Width,Screen_Height))

Light_Green = (144, 238, 144)
Dark_Green = (80, 200, 120)
Pixel_Size = 50

def Drawing_The_Grid():
    for y in range(0, Screen_Height, Pixel_Size):
        for x in range(0, Screen_Width, Pixel_Size):
            is_it_light_color = (x // Pixel_Size + y // Pixel_Size) % 2 == 0 
            if is_it_light_color:
                color = Light_Green
            else:
                color = Dark_Green
                
            square_drawing = pygame.Rect(x, y, Pixel_Size, Pixel_Size)
            pygame.draw.rect(screen, color, square_drawing)

Turnip_X = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
Turnip_Y = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
Random_Turnip_X = rand.choice(Turnip_X)
Random_Turnip_Y = rand.choice(Turnip_Y)

Image_Source  = "PumpkinCollectable.gif"
Game_Display_Image = pygame.image.load(Image_Source)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
    Drawing_The_Grid()
    screen.blit(Game_Display_Image, ((Random_Turnip_X), (Random_Turnip_Y)))
    pygame.display.flip()

pygame.quit()
