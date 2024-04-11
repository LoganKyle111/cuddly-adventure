import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shrunk")
screennum = 1

# Load images
bg_image = pygame.transform.scale2x(pygame.image.load("sprite_0.png"))
cave =  pygame.image.load("cave0.png")
cave_rect = cave.get_rect(center=(500,400))



def prompt(image):
    enter_prompt = pygame.image.load(image)
    prompt_rect = enter_prompt.get_rect(center=(500, 400))
    screen.blit(enter_prompt, prompt_rect)
    pygame.display.flip()

def screen_1():
    screen.blit(bg_image, (0, 0))
    screen.blit(cave, cave_rect)
    screen.blit(character[current_image_index], character_rect)


def screen_2():
    screen.blit(pygame.transform.scale2x(pygame.image.load("cavein0.png")), (0,0))



still = [pygame.transform.scale2x(pygame.image.load("sprite_00.png")), pygame.transform.scale2x(pygame.image.load("sprite_02.png")), pygame.transform.scale2x(pygame.image.load("sprite_01.png")), pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("sprite_01.png")),True, False)]
character_left = [pygame.transform.scale2x(pygame.image.load(f"LR_0{i}.png")) for i in range(0, 7)]
character_right = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load(f"LR_0{i}.png")), True, False) for i in range(0, 7)]
character_up = [pygame.transform.scale2x(pygame.image.load(f"up_0{i}.png")) for i in range(1, 4)]
character_down = [pygame.transform.scale2x(pygame.image.load(f"sprite_0{i+2}.png")) for i in range(1, 4)]
character = still


current_image_index = 0
character_rect = character[0].get_rect()
character_rect.center = (WIDTH // 2, HEIGHT - character_rect.height // 2)

# Set up movement variables
move_left = False
move_right = False
move_up = False
move_down = False
velocity = 5

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    if screennum == 1:
        screen_1()
    if screennum == 2:
        screen_2()
    pygame.display.flip()

    if move_right == True or move_left == True or move_up == True or move_down == True:
        move = True
    else:
        move = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and move == False:
                character = character_left
                move_left = True
            if event.key == pygame.K_d and move == False:
                character = character_right
                move_right = True
            if event.key == pygame.K_w and move == False:
                character = character_up
                move_up = True
            if event.key == pygame.K_s and move == False:
                character = character_down
                move_down = True
            if event.key == pygame.K_q and entercave == True:
                screennum = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a and move_left == True:
                character = still
                current_image_index = 2
                move_left = False
            if event.key == pygame.K_d and move_right == True:
                character = still
                current_image_index = 3
                move_right = False
            if event.key == pygame.K_w and move_up == True:
                character = still
                current_image_index = 1
                move_up = False
            if event.key == pygame.K_s and move_down == True:
                character = still
                current_image_index = 0
                move_down = False
    if character_rect.colliderect(cave_rect):
        prompt("display0.png")
        entercave = True
    else:
        entercave = False



    if move_left:
        character_rect.x -= velocity
        current_image_index = (current_image_index + 1) % len(character_left)

    if move_right:
        character_rect.x += velocity
        current_image_index = (current_image_index + 1) % len(character_right)

    if move_up:
        character_rect.y -= velocity
        current_image_index = (current_image_index + 1) % len(character_up)

    if move_down:
        character_rect.y += velocity
        current_image_index = (current_image_index + 1) % len(character_down)



    # Cap the frame rate
    clock.tick(12)