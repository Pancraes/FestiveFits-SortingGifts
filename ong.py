import pygame, sys, math, random
import levels, settings
import cv2

pygame.init()


WIDTH, HEIGHT = (1920, 1080)
FPS = 240
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("ppp.jpg").convert()
bg = pygame.transform.scale(bg, (1920, 1080))
dude = pygame.image.load("dude.png").convert_alpha()
dude = pygame.transform.scale(dude, (WIDTH // 2.5, HEIGHT // 2.5))


pygame.display.set_caption("Festive Fits and Sorted Gifts")


font = pygame.font.Font("Purisa Bold.ttf", 36)
t_font = pygame.font.Font("Purisa Bold.ttf", 48)


music = pygame.mixer.music.load("night.wav") # Music provided for free by Uppbeat
pygame.mixer.music.play(-1) #Infinite loop music
pygame.mixer.music.set_volume(0.1)


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
    return text_rect



def play_video(video_path):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    cap = cv2.VideoCapture(video_path)

    running = True
    while running:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], 'RGB')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(30)

    cap.release()


def main_menu():
    while True:
        

        screen.blit(bg, (0, 0))
        screen.blit(dude, (940, 450))


        title = "Festive Fits & Sorted Gifts"
        name = draw_text(title, t_font, BLACK, WIDTH // 2, 400)

        r1 = draw_text("Start Game", font, RED, WIDTH // 2, 550)
        button_1 = pygame.Rect(r1)
        
        r2 = draw_text("Settings", font, GREEN, WIDTH // 2, 650)
        button_2 = pygame.Rect(r1[0], r2[1], r1[2], r1[3])
        
        r3 = draw_text("Quit", font, BLUE, WIDTH // 2, 750)
        button_3 = pygame.Rect(r1[0], r3[1], r1[2], r1[3])

        mouse_pos= pygame.mouse.get_pos()       
        

        if button_1.collidepoint(mouse_pos):
            col1 = GREY
        else:
            col1 = WHITE

        if button_2.collidepoint(mouse_pos):
            col2 = GREY
        else:
            col2 = WHITE

        if button_3.collidepoint(mouse_pos):
            col3 = GREY
        else:
            col3 = WHITE

        pygame.draw.rect(screen, col1, button_1, 2)
        pygame.draw.rect(screen, col2, button_2, 2)
        pygame.draw.rect(screen, col3, button_3, 2)
        
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_1.collidepoint(mouse_pos):
                        play_video('INTRO.mp4')
                        levels.level_1(screen, event)
                        play_video('Timeline 1.mp4')
                        levels.level_2(screen, event)
                        play_video('Timeline 2.mp4')
                        levels.level_3(screen, event)
                        play_video('CONC.mp4')


                    elif button_2.collidepoint(mouse_pos):
                        settings.settings(screen, event)


                    elif button_3.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()


        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

main_menu()