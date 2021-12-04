import pygame
pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
car_width = 73
car_height = 108
gameDisplay = pygame.display.set_mode((display_width ,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('./차.jpg')

def car (carImg, x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def massage_display(text):
    LargeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, LargeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
def crash():
    massage_display('you gg')
def game_Loop():
    x = (display_width * 0.45)  # 10
    y = (display_width * 0.8)  # 10
    x = 0
    y = 0
    x_change = 0
    y_change = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change  # x = x+x_change
        y += y_change
        gameDisplay.fill(white)
        car(carImg, x, y)

        if x > display_width - car_width or x < 0 or y > display_height - car_height or y < 0 :
            crash()

        pygame.display.update()
        clock.tick(60)
game_Loop()
pygame.quit()
quit()
