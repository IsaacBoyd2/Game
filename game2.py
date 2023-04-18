import pygame
import sys
import random

####################
#Read me
#
#This is a game!
#
# Goals:
#       1. Make it so that the character can pick up the rocks.
#       2. Either make an inventory, or something next to your character that keeps track of the number of rocks you have.
#       3. Implement placing rocks
#       4. Implement block synergies?
# Ideas:
#       1. Make enemies that come towards you
#       2. Add some sort of score?
#       3. Farming?
#####################

def rock():                                      
    rectangle_w = random.randint(0, screen_info.current_w)                       #Set random size and posistion
    rectangle_h = random.randint(0, screen_info.current_h)
    rectangle_x = random.randint(10, 20)
    rectangle_y = random.randint(10, 20)
    
    rock = pygame.Rect(rectangle_w,rectangle_h,rectangle_x,rectangle_y)         #make the rock
    rock_list.append(rock)

def rock_spawning():
    spawn_chance = random.randint(1, int(rock_spawn_rate*(1+(len(rock_list)*0.1))))
    if spawn_chance == 50:
        rock()

# Initialize Pygame
pygame.init()

# Set the size of the window
screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(screen_size)

#Statics
screen.fill((0, 0, 0))      #Background
rock_list = []              #Store rocks
rock_position_list = []     #Store thier initial posistion.
rock_spawn_rate = 2000      #Larger is more rare
player_hitbox = pygame.Rect(screen_size[0]/2,screen_size[1]/2,10,10)

# Create the hamburger menu
hamburger_interact = pygame.Rect(screen_size[0]-40, 0, 20, 36)
hamburger_upper = pygame.Rect(screen_size[0]-40, 10, 20, 6)
hamburger_middle = pygame.Rect(screen_size[0]-40, 20, 20, 6)
hamburger_lower = pygame.Rect(screen_size[0]-40, 30, 20, 6)
hamburger_flag = True

#Inner hamburger menu
quit_button = pygame.Rect(screen_size[0]-70, 50, 60, 30)
font = pygame.font.Font(None, 24)
text_surface = font.render("Quit", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=quit_button.center)

#Scoreboard
holding_rectangle = pygame.Rect(screen_size[0]/2-100, 15, 200, 100)
score_font = pygame.font.Font(None, 40)
score = 0
text_surface_score = score_font.render(f"Score: {score}", True, (255, 255, 255))   #scoreboard

#Movement Speed
scroll_speed = 1     #Speed multipier
speed = 18           #Base speed


# Game loop
while True:

    
    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
                #Open and close menu
                if hamburger_interact.collidepoint(event.pos) and hamburger_flag == True:
                    hamburger_flag = False
                    

                elif hamburger_interact.collidepoint(event.pos) and hamburger_flag == False:
                    hamburger_flag = True

                #Quit
                if quit_button.collidepoint(event.pos) and hamburger_flag == False:
                        pygame.quit()
                        sys.exit()


        # Assemble the game
        pygame.draw.rect(screen, (0, 0, 0), hamburger_interact)     #Hamburger Menu
        pygame.draw.rect(screen, (255, 255, 255), hamburger_upper)
        pygame.draw.rect(screen, (255, 255, 255), hamburger_middle)
        pygame.draw.rect(screen, (255, 255, 255), hamburger_lower)

        

        text_surface_score = score_font.render(f"Score: {score}", True, (255, 255, 255))   #scoreboard
        text_rect_score = text_surface.get_rect(center=holding_rectangle.center)
        pygame.draw.rect(screen, (0,0,0), holding_rectangle)
        screen.blit(text_surface_score, (screen_size[0]/2-100,15))

        if hamburger_flag == False:                                 #Quit Button
            pygame.draw.rect(screen, (150, 0, 0), quit_button)
            screen.blit(text_surface, text_rect)

        if hamburger_flag == True:
            pygame.draw.rect(screen, (0, 0, 0), quit_button)

        

    for i in range(len(rock_list)):

        #Check if arrow keys are down.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pygame.draw.rect(screen, (0, 0, 0), rock_list[i])
            rock_list[i].x -= scroll_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pygame.draw.rect(screen, (0, 0, 0), rock_list[i])
            rock_list[i].x += scroll_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pygame.draw.rect(screen, (0, 0, 0), rock_list[i])
            rock_list[i].y -= scroll_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pygame.draw.rect(screen, (0, 0, 0), rock_list[i])
            rock_list[i].y += scroll_speed

        if player_hitbox.colliderect(rock_list[i]):
            score += 1

        pygame.draw.rect(screen, (255, 255, 255), rock_list[i])                            #Rock

    rock_spawning()
    pygame.draw.circle(screen, (255, 0, 0), (screen_size[0]/2,screen_size[1]/2),10)        #Player

    

    # Update the screen
    pygame.display.update()



    

    
    
