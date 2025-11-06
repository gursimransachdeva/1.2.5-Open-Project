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
Player_Color = "blue"
Player_X = 0
Player_Y = 0


Snake_Image_Source = "Snake.gif" 
Player_Image = pygame.image.load(Snake_Image_Source)
Player_Image = pygame.transform.scale(Player_Image, (Pixel_Size, Pixel_Size)) 
'''
Gemini helped me in the code on the lines 17-20. I fixed the transform.scale part. 
This line of code resizes the image so that it can fit in the pixel I created on the grid
'''

def Player():
    screen.blit(Player_Image, (Player_X , Player_Y))

def Player_Right():
    global Player_X
    global Player_Y 
    if Player_X + Pixel_Size < Screen_Width:
        Player_X = Player_X + Pixel_Size

def Player_Left():
    global Player_X
    global Player_Y 
    if Player_X - Pixel_Size >= 0:
        Player_X = Player_X - Pixel_Size

def Player_Up():
    global Player_X
    global Player_Y 
    if Player_Y - Pixel_Size < Screen_Height:
        Player_Y = Player_Y - Pixel_Size

def Player_Down():
    global Player_X
    global Player_Y
    if Player_Y + Pixel_Size >= 0:
        Player_Y = Player_Y + Pixel_Size


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

Apple_X = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
Apple_Y = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
Random_Apple_X = rand.choice(Apple_X)
Random_Apple_Y = rand.choice(Apple_Y)

Image_Source  = "AppleCollectable.gif"
Game_Display_Image = pygame.image.load(Image_Source)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player_Up()
            elif event.key == pygame.K_DOWN: 
                Player_Down()
            elif event.key == pygame.K_RIGHT:
                Player_Right()
            elif event.key == pygame.K_LEFT:
                Player_Left() 
    Drawing_The_Grid()
    screen.blit(Game_Display_Image, ((Random_Apple_X), (Random_Apple_Y)))
    Player()
    pygame.display.flip()

pygame.quit()
