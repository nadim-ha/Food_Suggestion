import pygame , random

#initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Food selector")

#set food list
dishes = ["Lablebi","ojja","Couscous","Kafteji","Pasta","Noodels","Lasagne","Lentil Soupe","Kleya","cooked salad","Vegetables omlette","Pizza"]

#Define colors
GREEN = (0, 255, 0)

#define fonts
custom_font = pygame.font.Font('BlackgroundsRegular.ttf', 65)

#select food from the list
food = random.choice(dishes)
print(food)

#define text:
custom_text = custom_font.render(food, True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#blit the text surface
display_surface.blit(custom_text, custom_text_rect)

#update display
pygame.display.flip()

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


#end the game
pygame.quit()