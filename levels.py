import pygame
import sys
import random

FPS = 240

def get_composite_mask(image):
    mask = pygame.mask.from_surface(image)
    width, height = image.get_size()

    combined_mask = pygame.mask.Mask((width, height))
    combined_mask.clear() 

    for x in range(width):
        for y in range(height):
            if mask.get_at((x, y)):
                combined_mask.set_at((x, y), 1)

    return combined_mask


# Constants and functions here
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
RED = (255, 0, 0)

def level_1(screen, event):
    
    suitcase = pygame.image.load('1st level assets/IMG_1091.png').convert_alpha()
    bg1 = pygame.image.load('1st level assets/luggagebackground.png').convert_alpha()
    hand_image = pygame.image.load('first1.png').convert_alpha()
    fist_image = pygame.image.load('second1.png').convert_alpha()
    

    images = [pygame.image.load(f'1st level assets/IMG_1{i}.png').convert_alpha() for i in range(100, 119)]
    rects = [images[i].get_rect(center=(560 + random.randint(0, 800), 340 + random.randint(0, 400))) for i in range(19)]
    composite_masks = [get_composite_mask(image) for image in images]

    dragging = False
    offset_x, offset_y = 0, 0
    drag_rect = None
    hand_is_fist = False

    
    # Hide the cursor
    pygame.mouse.set_visible(False)

    while not all([-30 < x.top < 30 and -30 < x.left < 30 for x in rects]):
        pos = pygame.mouse.get_pos()
        hand_rect = hand_image.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, rect in enumerate(rects):
                    composite_mask = composite_masks[i]
                    if rect.collidepoint(pos) and composite_mask.get_at((pos[0] - rect.x, pos[1] - rect.y)):
                        dragging = True
                        drag_rect = rect
                        offset_x = pos[0] - rect.centerx
                        offset_y = pos[1] - rect.centery

                        hand_is_fist = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False
                drag_rect = None

                hand_is_fist = False

            if dragging and event.type == pygame.MOUSEMOTION:
                if drag_rect is not None:
                    drag_rect.center = event.pos[0] - offset_x, event.pos[1] - offset_y

        screen.blit(bg1, (0, 0))
        screen.blit(suitcase, (0, 0))


        for i, image in enumerate(images):
            screen.blit(image, rects[i])

        if hand_is_fist:
            screen.blit(fist_image, (pos[0] - 100, pos[1]-100))
        else:
            screen.blit(hand_image, (pos[0] - 100, pos[1]-100))

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)





def level_2(screen, event):
    tray = pygame.image.load('2nd level assets/IMG_1144.png').convert_alpha()
    bg1 = pygame.image.load('2nd level assets/backgroundairplane.png').convert_alpha()
    images = [pygame.image.load(f'2nd level assets/IMG_11{i}.png').convert_alpha() for i in range(45, 54)]
    rects = [images[i].get_rect(center=(560 + random.randint(0, 800), 340 + random.randint(0, 400))) for i in range(9)]
    composite_masks = [get_composite_mask(image) for image in images]
    hand_image = pygame.image.load('first1.png').convert_alpha()
    fist_image = pygame.image.load('second1.png').convert_alpha()

    dragging = False
    offset_x, offset_y = 0, 0
    drag_rect = None
    hand_is_fist = False

    while not all([-30 < x.top < 30 and -30 < x.left < 30 for x in rects]):
        pos = pygame.mouse.get_pos()
        hand_rect = hand_image.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, rect in enumerate(rects):
                    composite_mask = composite_masks[i]
                    if rect.collidepoint(pos) and composite_mask.get_at((pos[0] - rect.x, pos[1] - rect.y)):
                        dragging = True
                        drag_rect = rect
                        offset_x = pos[0] - rect.centerx
                        offset_y = pos[1] - rect.centery
                        hand_is_fist = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False
                drag_rect = None
                hand_is_fist = False

            if dragging and event.type == pygame.MOUSEMOTION:
                if drag_rect is not None:
                    drag_rect.center = event.pos[0] - offset_x, event.pos[1] - offset_y

        screen.blit(bg1, (0, 0))
        screen.blit(tray, (0, 0))

        for i, image in enumerate(images):
            screen.blit(image, rects[i])

        if hand_is_fist:
            screen.blit(fist_image, (pos[0] - 100, pos[1]-100))
        else:
            screen.blit(hand_image, (pos[0] - 100, pos[1]-100))

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


def level_3(screen, event):
    bg1 = pygame.image.load('3rd level assets/giftbackground.png').convert_alpha()
    images = [pygame.image.load(f'3rd level assets/IMG_11{i}.png').convert_alpha() for i in range(34, 43)]
    rects = [images[i].get_rect(center=(900 + random.randint(0, 600), 540)) for i in range(4)]
    rects += [images[i].get_rect(center=(400 + random.randint(0, 600), 540)) for i in range(4, 9)] #
    composite_masks = [get_composite_mask(image) for image in images]
    hand_image = pygame.image.load('first1.png').convert_alpha()
    fist_image = pygame.image.load('second1.png').convert_alpha()

    dragging = False
    offset_x, offset_y = 0, 0
    drag_rect = None
    hand_is_fist = False

    while not all([-100 < x.top < 100 and -50 < x.left < 50 for x in rects]):
        pos = pygame.mouse.get_pos()
        hand_rect = hand_image.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, rect in enumerate(rects):
                    composite_mask = composite_masks[i]
                    if rect.collidepoint(pos) and composite_mask.get_at((pos[0] - rect.x, pos[1] - rect.y)):
                        dragging = True
                        drag_rect = rect
                        offset_x = pos[0] - rect.centerx
                        offset_y = pos[1] - rect.centery
                        hand_is_fist = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False
                drag_rect = None
                hand_is_fist = False

            if dragging and event.type == pygame.MOUSEMOTION:
                if drag_rect is not None:
                    drag_rect.center = event.pos[0] - offset_x, event.pos[1] - offset_y

        screen.blit(bg1, (0, 0))

        for i, image in enumerate(images):
            screen.blit(image, rects[i])

        if hand_is_fist:
            screen.blit(fist_image, (pos[0] - 100, pos[1]-100))
        else:
            screen.blit(hand_image, (pos[0] - 100, pos[1]-100))

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)