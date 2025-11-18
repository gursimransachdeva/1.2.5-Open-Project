import pygame # type: ignore
import random as rand
import time 

pygame.init()
BLACK = (0, 0, 0) 
FONT_SIZE = 30
SCORE_FONT = pygame.font.Font(None, FONT_SIZE)
Screen_Width = 750
Screen_Height = 750
screen = pygame.display.set_mode((Screen_Width, Screen_Height))

Light_Green = (144, 238, 144)
Dark_Green = (80, 200, 120)
Pixel_Size = 50
Clock = pygame.time.Clock() 
SNAKE_SPEED = 10 
Game_Over = False

Snake_Body = [(0, 0)]
Snake_Direction = "RIGHT"
Next_Direction = "RIGHT"
Player_Score = 0

Snake_Image_Source = "Snake.gif" 
Player_Image = pygame.image.load(Snake_Image_Source)
Player_Image = pygame.transform.scale(Player_Image, (Pixel_Size, Pixel_Size))
Snake_Body_Image_Source = "Snake_Body.gif"
Snake_Body_Image = pygame.image.load(Snake_Body_Image_Source)
Snake_Body_Image = pygame.transform.scale(Snake_Body_Image, (Pixel_Size, Pixel_Size))
Image_Source = "AppleCollectable.gif"
Game_Display_Image = pygame.image.load(Image_Source)
Game_Display_Image = pygame.transform.scale(Game_Display_Image, (Pixel_Size, Pixel_Size))

Grid_Coords = list(range(0, Screen_Width, Pixel_Size))

def generate_new_apple_position():
    while True:
        x = rand.choice(Grid_Coords)
        y = rand.choice(Grid_Coords)
        if (x, y) not in Snake_Body:
            return x, y
Random_Apple_X, Random_Apple_Y = generate_new_apple_position()

def Drawing_The_Grid():
    for y in range(0, Screen_Height, Pixel_Size):
        for x in range(0, Screen_Width, Pixel_Size):
            is_it_light_color = (x // Pixel_Size + y // Pixel_Size) % 2 == 0 
            color = Light_Green if is_it_light_color else Dark_Green
            square_drawing = pygame.Rect(x, y, Pixel_Size, Pixel_Size)
            pygame.draw.rect(screen, color, square_drawing)

def Draw_Snake():
    for index, (segment_x, segment_y) in enumerate(Snake_Body):
        if index == 0:
            screen.blit(Player_Image, (segment_x, segment_y))
        else:
            screen.blit(Snake_Body_Image, (segment_x, segment_y))

def Snake_Head_To_Body_Collision():
    head_position = Snake_Body[0]
    body_segments = Snake_Body[1:] 
    if head_position in body_segments:
        return True
    return False

def Check_Wall_Collision():
    """Checks if the snake's head goes outside the screen boundaries."""
    head_x, head_y = Snake_Body[0]
    if head_x < 0 or head_x >= Screen_Width or head_y < 0 or head_y >= Screen_Height:
        return True
    return False

def Draw_Apple():
    screen.blit(Game_Display_Image, (Random_Apple_X, Random_Apple_Y))
def move_snake():
    global Snake_Body
    global Snake_Direction
    global Next_Direction
    
    Snake_Direction = Next_Direction
    
    head_x, head_y = Snake_Body[0]
    new_head_x, new_head_y = head_x, head_y
    if Snake_Direction == "RIGHT":
        new_head_x = new_head_x + Pixel_Size
    elif Snake_Direction == "LEFT":
        new_head_x -= Pixel_Size
    elif Snake_Direction == "UP":
        new_head_y -= Pixel_Size
    elif Snake_Direction == "DOWN":
        new_head_y += Pixel_Size
    new_head = (new_head_x, new_head_y)
    ate_apple = new_head_x == Random_Apple_X and new_head_y == Random_Apple_Y
    Snake_Body.insert(0, new_head) 
    if not ate_apple:
        Snake_Body.pop() 
    return ate_apple 
'''For lines above (the if, elif statements) I used AI, but I changed up the variable names to make it more descriptive. 
What the code does is that it changes the direction of the sprite so that it can go in one direction in the area
the user wishes it to go to. '''
def handle_collectable(ate_apple):
    global Random_Apple_X
    global Random_Apple_Y
    global Player_Score

    if ate_apple:
        Player_Score = Player_Score + 1
        Random_Apple_X, Random_Apple_Y = generate_new_apple_position()

running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if not Game_Over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Snake_Direction != "DOWN":
                Next_Direction = "UP"
            elif event.key == pygame.K_DOWN and Snake_Direction != "UP": 
                Next_Direction = "DOWN"
            elif event.key == pygame.K_RIGHT and Snake_Direction != "LEFT":
                Next_Direction = "RIGHT"
            elif event.key == pygame.K_LEFT and Snake_Direction != "RIGHT":
                Next_Direction = "LEFT"
    
    if not Game_Over:
        frame_count = frame_count + 1

    if frame_count % SNAKE_SPEED == 0:
        ate_apple = move_snake()
        handle_collectable(ate_apple)
        if Snake_Head_To_Body_Collision() or Check_Wall_Collision():
                Game_Over = True
    
    if Game_Over == True:
        Player_Score = "You Died!"
   
    Drawing_The_Grid()
    Draw_Apple()
    Draw_Snake()
    score_text = str(Player_Score)
    score_surface = SCORE_FONT.render(score_text, True, BLACK) 
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    screen.blit(score_surface, score_rect)
    pygame.display.flip()
    Clock.tick(60)

pygame.quit()
