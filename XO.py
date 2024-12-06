import pygame
import time

pygame.init()
pygame.display.set_caption("XO")

BLACK = ((0, 0, 0))
WHITE = ((255, 255, 255))
HEIGHT = 600
WHIDTH = 600
FPS = 60
s = 0
cases = 0
ORANGE = (255, 165, 0)
GREEN = ((0, 200, 50))
RED = ((200, 0, 0))
criteria = False
confir = False
choix1 = 1
choix2 = 1
choix3 = 1
choix4 = 1
choix5 = 1
choix6 = 1
choix7 = 1
choix8 = 1
choix9 = 1
player = [False, False, False, False, False, False, False, False, False]
bot = [False, False, False, False, False, False, False, False, False]

def robot(choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9):
    global liste, special
    print("go")

    #attaquer
    elif choix1 == 3 and choix2 == 3 and choix3 == 1:
        choix3 = 3
    elif choix1 == 3 and choix3 == 3 and choix2 == 1:
        choix2 = 3
    elif choix2 == 3 and choix3 == 3 and choix1 == 1:
        choix1 = 3
    elif choix1 == 3 and choix5 == 3 and choix9 == 1:
        choix9 = 3
    elif choix9 == 3 and choix1 == 3 and choix5 == 1:
        choix5 = 3
    elif choix7 == 3 and choix3 == 3 and choix5 == 1:
        choix5 = 3
    elif choix4 == 3 and choix5 == 3 and choix6 == 1:
        choix6 = 3
    elif choix4 == 3 and choix6 == 3 and choix5 == 1:
        choix5 = 3
    elif choix5 == 3 and choix6 == 3 and choix4 == 1:
        choix4 = 3
    elif choix7 == 3 and choix8 == 3 and choix9 == 1:
        choix9 = 3
    elif choix7 == 3 and choix9 == 3 and choix8 == 1:
        choix8 = 3
    elif choix8 == 3 and choix9 == 3 and choix7 == 1:
        choix7 = 3
    elif choix4 == 3 and choix7 == 3 and choix1 == 1:
        choix1 = 3
    elif choix1 == 3 and choix7 == 3 and choix4 == 1:
        choix4 = 3
    elif choix1 == 3 and choix4 == 3 and choix7 == 1:
        choix7 = 3
    elif choix5 == 3 and choix8 == 3 and choix2 == 1:
        choix2 = 3
    elif choix2 == 3 and choix8 == 3 and choix5 == 1:
        choix5 = 3
    elif choix2 == 3 and choix5 == 3 and choix8 == 1:
        choix8 = 3
    elif choix7 == 3 and choix5 == 3 and choix3 == 1:
        choix3 = 3
    elif choix3 == 3 and choix5 == 3 and choix7 == 1:
        choix7 = 3
    elif choix6 == 3 and choix9 == 3 and choix3 == 1:
        choix3 = 3
    elif choix3 == 3 and choix9 == 3 and choix6 == 1:
        choix6 = 3
    elif choix3 == 3 and choix6 == 3 and choix9 == 1:
        choix9 = 3
    elif choix9 == 3 and choix5 == 3 and choix1 == 1:
        choix1 = 3
    
    
    

    #contrer
    if choix1 == 0 and choix2 == 0 and choix3 == 1:
        choix3 = 3
    
    elif choix1 == 0 and choix3 == 0 and choix2 == 1:
        choix2 = 3
    elif choix2 == 0 and choix3 == 0 and choix1 == 1:
        choix1 = 3
    elif choix1 == 0 and choix5 == 0 and choix9 == 1:
        choix9 = 3
    elif choix9 == 0 and choix1 == 0 and choix5 == 1:
        choix5 = 3
    elif choix7 == 0 and choix3 == 0 and choix5 == 1:
        choix5 = 3
    elif choix4 == 0 and choix5 == 0 and choix6 == 1:
        choix6 = 3
    elif choix4 == 0 and choix6 == 0 and choix5 == 1:
        choix5 = 3
    elif choix5 == 0 and choix6 == 0 and choix4 == 1:
        choix4 = 3
    elif choix7 == 0 and choix8 == 0 and choix9 == 1:
        choix9 = 3
    elif choix7 == 0 and choix9 == 0 and choix8 == 1:
        choix8 = 3
    elif choix8 == 0 and choix9 == 0 and choix7 == 1:
        choix7 = 3
    elif choix4 == 0 and choix7 == 0 and choix1 == 1:
        choix1 = 3
    elif choix1 == 0 and choix7 == 0 and choix4 == 1:
        choix4 = 3
    elif choix1 == 0 and choix4 == 0 and choix7 == 1:
        choix7 = 3
    elif choix5 == 0 and choix8 == 0 and choix2 == 1:
        choix2 = 3
    elif choix2 == 0 and choix8 == 0 and choix5 == 1:
        choix5 = 3
    elif choix2 == 0 and choix5 == 0 and choix8 == 1:
        choix8 = 3
    elif choix7 == 0 and choix5 == 0 and choix3 == 1:
        choix3 = 3
    elif choix3 == 0 and choix5 == 0 and choix7 == 1:
        choix7 = 3
    elif choix6 == 0 and choix9 == 0 and choix3 == 1:
        choix3 = 3
    elif choix3 == 0 and choix9 == 0 and choix6 == 1:
        choix6 = 3
    elif choix3 == 0 and choix6 == 0 and choix9 == 1:
        choix9 = 3
    elif choix9 == 0 and choix5 == 0 and choix1 == 1:
        choix1 = 3
    
    
    
    
    
    elif choix7 == 0 and choix2 == 0 and choix4 == 1:
        choix4 = 3
    elif choix8 == 0 and choix3 == 0 and choix6 == 1:
        choix6 = 3
    elif choix3 == 0 and choix4 == 0 and choix2 == 1:
        choix2 = 3
    elif choix6 == 0 and choix7 == 0 and choix1 == 1:
        choix1 = 3
    elif choix1 == 0 and choix2 == 1:
        choix3 = 3
    elif choix4 == 0 and choix1 == 1:
        choix1 = 3
    elif choix4 == 0 and choix2 == 1:
        choix2 = 3
    elif choix5 == 0 and choix7 == 1:
        choix7 = 3
    elif choix8 == 0 and choix9 == 1:
        choix9 = 3
    elif choix7 == 0 and choix9 == 1:
        choix9 = 3
    elif choix4 == 0 and choix6 == 1:
        choix6 = 3
    elif choix8 == 0 and choix7 == 1:
        choix7 = 3
    elif choix6 == 0 and choix2 == 1:
        choix2 = 3
    elif choix9 == 0 and choix6 == 1:
        choix6 = 3
    elif choix9 == 0 and choix4 == 1:
        choix4 = 3
    elif choix6 == 0 and choix8 == 1:
        choix8 = 3
    elif choix1 == 0 or choix2 == 0 or choix3 == 0 or choix4 == 0 or choix6 == 0 or choix7 == 0 or choix8 == 0 or choix9 == 0:
        if choix1 == 1:
            choix1 = 3
        elif choix2 == 1:
            choix2 = 3
        elif choix3 == 1:
            choix3 = 3
        elif choix4 == 1:
            choix4 = 3
        elif choix5 == 1:
            choix5 = 3
        elif choix6 == 1:
            choix6 = 3
        elif choix7 == 1:
            choix7 = 3
        elif choix8 == 1:
            choix8 = 3
        elif choix9 == 1:
            choix9 = 3
        print("derniere option")
        
    else:
        print("ERREUR")
    
        
    
    
    time.sleep(0.2)
    print(choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9)
    return choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9


ecran = pygame.display.set_mode((HEIGHT, WHIDTH))
ecran.fill((0, 0, 0))


def main():
    global criteria, choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9, s, bot, player, cases, confir
    clock = pygame.time.Clock()
    run = True
    fond = pygame.font.Font(None, 160)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                criteria = True
                mouse_x, mouse_y = event.pos
                if 0 <= mouse_x <= 200 and 0 <= mouse_y <= 200:
                    print("GO")
                    if choix1 == 1:
                        choix1 = 0
                        if bot[0] != True:
                            player[0] = True
                if 200 <= mouse_x <= 400 and 0 <= mouse_y <= 200:
                    if choix2 == 1:
                        choix2 = 0
                        if bot[1] != True:
                            player[1] = True
                if 400 <= mouse_x <= 600 and 0 <= mouse_y <= 200:
                    if choix3 == 1:
                        choix3 = 0
                        if bot[2] != True:
                            player[2] = True
                if 0 <= mouse_x <= 200 and 200 <= mouse_y <= 400:
                    if choix4 == 1:
                        choix4 = 0
                        if bot[3] != True:
                            player[3] = True
                if 200 <= mouse_x <= 400 and 200 <= mouse_y <= 400:
                    if choix5 == 1:
                        choix5 = 0
                        if bot[4] != True:
                            player[4] = True
                if 400 <= mouse_x <= 600 and 200 <= mouse_y <= 400:
                    if choix6 == 1:
                        choix6 = 0
                        if bot[5] != True:
                            player[5] = True
                if 0 <= mouse_x <= 200 and 400 <= mouse_y <= 600:
                    if choix7 == 1:
                        choix7 = 0
                        if bot[6] != True:
                            player[6] = True
                if 200 <= mouse_x <= 400 and 400 <= mouse_y <= 600:
                    if choix8 == 1:
                        choix8 = 0
                        if bot[7] != True:
                            player[7] = True
                if 400 <= mouse_x <= 600 and 400 <= mouse_y <= 600:
                    if choix9 == 1:
                        choix9 = 0
                        if bot[8] != True:
                            player[8] = True

        ecran.fill((0, 0, 0))
        if choix1 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix1 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[0] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 6, HEIGHT // 5))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix2 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix2 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[1] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HEIGHT // 5))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix3 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix3 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[2] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 1.2, HEIGHT // 5))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix4 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix4 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[3] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 6, HEIGHT // 2))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix5 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix5 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[4] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HEIGHT // 2))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix6 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix6 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[5] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 1.2, HEIGHT // 2))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix7 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix7 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[6] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 6, HEIGHT // 1.2))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix8 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix8 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[7] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HEIGHT // 1.2))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        if choix9 != 1:
            text_surface = fond.render("X", True, WHITE)
            if choix9 == 3:
                text_surface = fond.render("O", True, WHITE)
                bot[8] = True
            text_rect = text_surface.get_rect(center=(WHIDTH // 1.2, HEIGHT // 1.2))
            ecran.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
        
        if criteria == True:
            choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9 = robot(choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9)
        pygame.draw.line(ecran, WHITE, (570, 200), (40, 200), 3)
        pygame.draw.line(ecran, WHITE, (570, 400), (40, 400), 3)
        pygame.draw.line(ecran, WHITE, (200, 570), (200, 40), 3)
        pygame.draw.line(ecran, WHITE, (400, 570), (400, 40), 3)


        for i in zip(player, bot):
            if i[0] == True or i[1] == True:
                s += 1
            
                
                    
            if (bot[0] == True and bot[1] == True and bot[2] == True) or\
                        (bot[3] == True and bot[4] == True and bot[5] == True) or\
                        (bot[6] == True and bot[7] == True and bot[8] == True) or\
                        (bot[0] == True and bot[3] == True and bot[6] == True) or\
                        (bot[1] == True and bot[4] == True and bot[7] == True) or\
                        (bot[2] == True and bot[5] == True and bot[8] == True) or\
                        (bot[0] == True and bot[4] == True and bot[8] == True) or\
                        (bot[2] == True and bot[4] == True and bot[6] == True):
                        cases += 1
            if (player[0] == True and player[1] == True and player[2] == True) or\
                        (player[3] == True and player[4] == True and player[5] == True) or\
                        (player[6] == True and player[7] == True and player[8] == True) or\
                        (player[0] == True and player[3] == True and player[6] == True) or\
                        (player[1] == True and player[4] == True and player[7] == True) or\
                        (player[2] == True and player[5] == True and player[8] == True) or\
                        (player[0] == True and player[4] == True and player[8] == True) or\
                        (player[2] == True and player[4] == True and player[6] == True):
                        cases += 20
                        
            if cases > 0:        
                confir = True
                if cases == 1:
                            font = pygame.font.Font(None, 120)
                            text_surface = font.render(f"""GAME OVER""", True, RED)
                            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HEIGHT // 2))
                            ecran.blit(text_surface, text_rect)
                            pygame.display.update(text_rect)
                            time.sleep(2)
                elif cases == 20:
                            font = pygame.font.Font(None, 120)
                            text_surface = font.render(f"""WINNER!""", True, GREEN)
                            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HEIGHT // 2))
                            ecran.blit(text_surface, text_rect)
                            pygame.display.update(text_rect)
                            time.sleep(2)
                choix1 = 1
                choix2 = 1
                choix3 = 1
                choix4 = 1
                choix5 = 1
                choix6 = 1
                choix7 = 1
                choix8 = 1
                choix9 = 1
                bot = [False, False, False, False, False, False, False, False, False]
                player = [False, False, False, False, False, False, False, False, False]
                cases = 0
            if (s == 9 or s > 9) and confir == False:        
                
                        font = pygame.font.Font(None, 120)
                        text_surface = font.render(f"""DRAW!""", True, ORANGE)
                        text_rect = text_surface.get_rect(center=(WHIDTH // 2, HEIGHT // 2))
                        ecran.blit(text_surface, text_rect)
                        pygame.display.update(text_rect)
                        time.sleep(2)

                        choix1 = 1
                        choix2 = 1
                        choix3 = 1
                        choix4 = 1
                        choix5 = 1
                        choix6 = 1
                        choix7 = 1
                        choix8 = 1
                        choix9 = 1
                        bot = [False, False, False, False, False, False, False, False, False]
                        player = [False, False, False, False, False, False, False, False, False]
                        cases = 0
            
            confir = False
                    
                    
        s = 0
        criteria = False
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

