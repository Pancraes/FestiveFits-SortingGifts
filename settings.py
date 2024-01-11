import pygame, sys, random
from pygame.locals import *

pygame.init()

#CONSTANTS
WIDTH, HEIGHT = (1920, 1080)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)

FPS = 240

def settings(screen, event):
    
    import ong

    # Function to draw text
    def draw_text(text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)
        return text_rect

    # Fonts
    font = pygame.font.Font("Purisa Bold.ttf", 36)

    #background image
    bg = pygame.image.load("ppp.jpg").convert()
    bg = pygame.transform.scale(bg, (1920, 1080))
    clock = pygame.time.Clock()

    running = True
    v = False


    while running:

        screen.blit(bg, (0,0))
        m_pos = pygame.mouse.get_pos()


        #Back to menu button
        back = draw_text("Back", font, BLACK, 1550, 800)
        back_button = pygame.Rect(back)


        #Volume button
        volume = draw_text("Volume ON/OFF", font, BLACK, WIDTH // 2, HEIGHT // 2)
        volume_button = pygame.Rect(volume)
        if back_button.collidepoint(m_pos):
            col1 = GREY
        else:
            col1 = WHITE
        if volume_button.collidepoint(m_pos):
            col2 = GREY
        else:
            col2 = WHITE


        #Drawing the buttons
        pygame.draw.rect(screen, col1, back_button, 1)
        pygame.draw.rect(screen, col2, volume_button, 1)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button.collidepoint(m_pos):
                    ong.main_menu()

                if volume_button.collidepoint(m_pos):
                    v = not v
                    if v:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.play(-1)


        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()