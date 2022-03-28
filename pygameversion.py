import pygame
import os
from pygame.locals import *
from endgame.questions import *
from random import randint
import pygame.freetype



# pygame starts here
pygame.font.init()

# define general info
WIDTH, HEIGHT = 1200, 630
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorteerimine")
FPS = 60
TRASHWIDTH, TRASHHEIGHT = 200, 200

# define colors
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
TRASHCAN_TEXT_COLOR = (255, 255, 255)
QUESTION_TEXT_COLOR = (255, 255, 255)

# import fonts, define
pygame.freetype.init()
pixel_font =pygame.font.Font('dogicapixel.ttf', 80)



# define fonts
HEALTH_FONT = pygame.font.Font('dogicapixel.ttf', 25)
PLAYER_TEXT_FONT = pygame.font.Font('dogicapixel.ttf', 25)
START_GAME_FONT = pygame.font.Font('dogicapixel.ttf', 80)
BASE_FONT = pygame.font.Font('dogicapixel.ttf', 30) #text user
TRASHCAN_FONT = pygame.font.Font('dogicapixel.ttf',20)
QUESTION_FONT = pygame.font.Font('dogicapixel.ttf', 30)


# input field info
user_text = ''
input_rect = pygame.Rect(525, 350, 140, 40)
input_rect_box = pygame.draw.rect(SCREEN, GREY, input_rect)
color_active = pygame.Color('darkseagreen1')
color_passive = pygame.Color('darkseagreen4')
color = color_passive

# start game label
start_game_text = START_GAME_FONT.render("START GAME", True, WHITE)
START_GAME_BOX = pygame.Rect((WIDTH - start_game_text.get_width()) // 2, (HEIGHT - start_game_text.get_height()) // 2-25, start_game_text.get_width(), start_game_text.get_height()+10)


# startgame hitbox
startgamebox = pygame.draw.rect(SCREEN, GREY, START_GAME_BOX)

# define the background
BACKGROUND_IMAGE = pygame.image.load(os.path.join('pixelmets.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

# define the trashcan
TRASHCAN_IMAGE = pygame.image.load(os.path.join('trashcan.png'))
TRASHCAN = pygame.transform.scale(TRASHCAN_IMAGE, (TRASHWIDTH, TRASHHEIGHT))

# game stage
startgame = 0


# trashcan hitboxes

# metall ja plastik hitbox
trashcan_box = pygame.Rect(50, 610 - TRASHCAN.get_height() + 20, 120, 160)
metall_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# ohtlikjäätmed hitbox
trashcan_box = pygame.Rect(195, 610 - TRASHCAN.get_height() + 20, 120, 160)
ohtlik_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# biojäätmed hitbox
trashcan_box = pygame.Rect(340, 610 - TRASHCAN.get_height() + 20, 120, 160)
bio_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# papp ja paber hitbox
trashcan_box = pygame.Rect(475, 610 - TRASHCAN.get_height() + 20, 120, 160)
papp_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# klaas hitbox
trashcan_box = pygame.Rect(617, 610 - TRASHCAN.get_height() + 20, 120, 160)
klaas_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# olme hitbox
trashcan_box = pygame.Rect(755, 610 - TRASHCAN.get_height() + 20, 120, 160)
olme_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# jäätmejaam hitbox
trashcan_box = pygame.Rect(895, 610 - TRASHCAN.get_height() + 20, 120, 160)
jaatmejaam_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# Riide konteiner hitbox
trashcan_box = pygame.Rect(1035, 610 - TRASHCAN.get_height() + 20, 120, 160)
riide_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# järgmine ese hitbox
trashcan_box = pygame.Rect(540, 610 - TRASHCAN.get_height() - 140, 120, 160)
jargmine_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# restart game hitbox
restart_box = pygame.Rect((WIDTH - 450) // 2, (HEIGHT+105) // 2, 490, 85)
restart_hitbox = pygame.draw.rect(SCREEN, GREY, restart_box)


# starting screen
def starting_draw_window():
    # set global var
    global color

    SCREEN.blit(BACKGROUND, (0, 0))
    startgamebox = pygame.draw.rect(SCREEN, GREY, START_GAME_BOX,2)
    my_font = pygame.font.Font('dogicapixel.ttf', 80)  # Load font object.pixel_font =pygame.freetype.Font('pixelart.ttf', 80)
    text_image = my_font.render("START GAME", True, WHITE)  # Render text image.
    SCREEN.blit(text_image, ((WIDTH - text_image.get_width()) // 2, (HEIGHT - text_image.get_height()) // 2 - 20,)) # Draw image to screen.


    # start game input field colors
    if active:
        color = color_active
    else:
        color = color_passive

    # draw main
    pygame.draw.rect(SCREEN, color, input_rect,2)
    text_surface = BASE_FONT.render(user_text, True, color) #  user text
    SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 6))#  user text
    input_rect.w = max(150, text_surface.get_width() + 10)
    pygame.display.update()

def draw_window(lives, user_text, küsimus, oigeid):
    # background drawing
    SCREEN.blit(BACKGROUND, (0, 0))

    # health and name drawing
    lives = HEALTH_FONT.render("Elud: " + str(lives), True, WHITE)
    SCREEN.blit(lives, (WIDTH - lives.get_width() - 10, 60))
    user_text = HEALTH_FONT.render("Nimi: " + str(user_text), True, WHITE)
    SCREEN.blit(user_text, (WIDTH - user_text.get_width() - 10, 20))
    oigeid = HEALTH_FONT.render("Punktid: " + str(oigeid), True, WHITE)
    SCREEN.blit(oigeid, (WIDTH - oigeid.get_width() - 10, 100))

    # trashcan drawing


    # metall ja plastik prükikast
    SCREEN.blit(TRASHCAN, (10, 610 - TRASHCAN.get_height()))

    # metall ja plastik
    trashcan_text = TRASHCAN_FONT.render("Metall ja", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (40, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("plastik", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (55, 610 - TRASHCAN.get_height()+ 100))


    # ohtlikud jäätmed prükikast
    SCREEN.blit(TRASHCAN, (155, 610 - TRASHCAN.get_height()))

    # ohtlikud jäätmed
    trashcan_text = TRASHCAN_FONT.render("Ohtlikud", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (195, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jäätmed", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (200, 610 - TRASHCAN.get_height() + 100))


    # biojäätmed prükikast
    SCREEN.blit(TRASHCAN, (295, 610 - TRASHCAN.get_height()))

    # biojäätmed
    trashcan_text = TRASHCAN_FONT.render("Bio-", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (370, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jäätmed", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (340, 610 - TRASHCAN.get_height() + 100))


    # papp ja paber prükikast
    SCREEN.blit(TRASHCAN, (435, 610 - TRASHCAN.get_height()))

    # papp ja paber
    trashcan_text = TRASHCAN_FONT.render("Papp ja ", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (483, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("paber", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (495, 610 - TRASHCAN.get_height() + 100))


    # klaas prükikast
    SCREEN.blit(TRASHCAN, (575, 610 - TRASHCAN.get_height()))

    # klaas
    trashcan_text = TRASHCAN_FONT.render("Klaas", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (635, 610 - TRASHCAN.get_height() + 85))


    # olmejäätmed prükikast
    SCREEN.blit(TRASHCAN, (715, 610 - TRASHCAN.get_height()))

    # olmejäätmed
    trashcan_text = TRASHCAN_FONT.render("Olme-", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (775, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jäätmed", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (760, 610 - TRASHCAN.get_height() + 100))


    # jäätmejaam prükikast
    SCREEN.blit(TRASHCAN, (855, 610 - TRASHCAN.get_height()))

    # jäätmejaam
    trashcan_text = TRASHCAN_FONT.render("Jäätme-", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (900, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jaam", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (920, 610 - TRASHCAN.get_height() + 100))


    # Riide konteiner prükikast
    SCREEN.blit(TRASHCAN, (995, 610 - TRASHCAN.get_height()))

    # Riide konteiner
    trashcan_text = TRASHCAN_FONT.render("Riide", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (1060, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("konteiner", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (1030, 610 - TRASHCAN.get_height() + 100))


    # küsimus
    main_question_text = QUESTION_FONT.render(küsimus, True, QUESTION_TEXT_COLOR)
    SCREEN.blit(main_question_text, (50, 60))



    pygame.display.update()


# wrong answer screen
def draw_window_hint(hint):
    # background drawing
    SCREEN.blit(BACKGROUND, (0, 0))


    main_hint_text = QUESTION_FONT.render(hint, True, QUESTION_TEXT_COLOR)
    SCREEN.blit(main_hint_text, (50, 200))

    # jargmine ese
    SCREEN.blit(TRASHCAN, (500, 610 - TRASHCAN.get_height() - 160 ))

    # jargmine ese
    trashcan_text = TRASHCAN_FONT.render("Järgmine ese", True, TRASHCAN_TEXT_COLOR)
    SCREEN.blit(trashcan_text, (500, 610 - TRASHCAN.get_height()-60 ))

    pygame.display.update()


# game failed screen
def draw_window_gameover():
    # background drawing

    SCREEN.blit(BACKGROUND, (0, 0))

    # health and name drawing

    game_over_text = START_GAME_FONT.render("GAME OVER", True, WHITE)
    SCREEN.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, (HEIGHT-80) // 2 ))
    restart_text = START_GAME_FONT.render("RESTART", True, WHITE)
    SCREEN.blit(restart_text, ((WIDTH - 450) // 2, (HEIGHT + 120) // 2))
    pygame.draw.rect(SCREEN, WHITE, restart_hitbox, 2)


    pygame.display.update()

def draw_window_game_completed( user_text, oigeid):
    # background drawing
    SCREEN.blit(BACKGROUND, (0, 0))

    # health and name drawing

    game_completed_text = PLAYER_TEXT_FONT.render("Mängur: " + str(user_text) + ", läbis mängu " + str(oigeid) + " punktiga", True, WHITE)
    SCREEN.blit(game_completed_text, ((WIDTH - game_completed_text.get_width())// 2, HEIGHT // 2))
    game_over_text = START_GAME_FONT.render("GAME COMPLETED", True, WHITE)
    SCREEN.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, (HEIGHT - 200) // 2 ))
    restart_text = START_GAME_FONT.render("RESTART", True, WHITE)
    SCREEN.blit(restart_text, ((WIDTH - 450) // 2, (HEIGHT + 120) // 2))
    pygame.draw.rect(SCREEN, WHITE, restart_hitbox, 2)
    #WIDTH / 2 - restart_text.get_width() / 2
    pygame.display.update()

# set before main func
active = False

# main func
def main():
    # lists
    kusimused_list = [question1.question, question2.question, question3.question, question4.question, question5.question, question6.question, question7.question, question8.question, question9.question, question10.question, question11.question, question12.question, question13.question, question14.question, question15.question, question16.question, question17.question, question18.question, question19.question, question20.question]
    oiged_list = [question1.right_answer, question2.right_answer, question3.right_answer, question4.right_answer, question5.right_answer, question6.right_answer, question7.right_answer, question8.right_answer, question9.right_answer, question10.right_answer, question11.right_answer, question12.right_answer, question13.right_answer, question14.right_answer, question15.right_answer, question16.right_answer, question17.right_answer, question18.right_answer, question19.right_answer, question20.right_answer]
    hint_list = [question1.hint, question2.hint, question3.hint, question4.hint, question5.hint, question6.hint, question7.hint, question8.hint, question9.hint, question10.hint, question11.hint, question12.hint, question13.hint, question14.hint, question15.hint, question16.hint, question17.hint, question18.hint, question19.hint, question20.hint]
    koik_kusimused = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20]

    # randomise
    randomized_questions_list = []
    randomized_answers_list = []
    randomized_hint_list = []

    # küsimuste küsimis loop ja delete
    for i in koik_kusimused:
        # ask
        randomnumber = randint(0, len(kusimused_list) - 1)
        randomized_questions_list.append(kusimused_list[randomnumber])
        randomized_answers_list.append(oiged_list[randomnumber])
        randomized_hint_list.append(hint_list[randomnumber])

        # delete the already printed
        del kusimused_list[randomnumber]
        del oiged_list[randomnumber]
        del hint_list[randomnumber]

    # set global vars
    global user_text
    global active

    # define vars
    startgame = 0
    lives = 3
    oigeid = 0
    number_question = 0

    # set delay
    clock = pygame.time.Clock()

    # main loop
    run = True

    while run:
        # get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # set frame time
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # if start screen , select/deselect input field
            if startgame == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_box.collidepoint(mouse_pos):
                        active = True
                    else:
                        active = False

            #start screen
            if event.type == pygame.KEYDOWN:#usertext
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode#usertext

            # press on input field ,start screen
            if startgame == 0:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if startgamebox.collidepoint(mouse_pos):
                            startgame =1
        if startgame == 1:

            if number_question == number_question:
                hint = randomized_hint_list[number_question]
                küsimus = randomized_questions_list[number_question]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:

                    # trashcan clicks, ask which can and if correct
                    if metall_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "metall ja plastik":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif ohtlik_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "ohtlikud jäätmed":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif bio_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "biojäätmed":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif papp_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "papp ja paber":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif klaas_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "klaas":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif olme_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "olmejäätmed":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif jaatmejaam_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "jäätmejaam":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                    elif riide_trashcan_hitbox.collidepoint(mouse_pos):
                        if randomized_answers_list[number_question] == "riide konteiner":
                            number_question += 1
                            oigeid += 1
                        else:
                            lives -= 1
                            startgame = 4
                pygame.time.wait(250)


        if number_question == len(koik_kusimused):
            startgame = 3

        # when game end, restart
        if startgame == 3:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if restart_hitbox.collidepoint(mouse_pos):
                        main()
                pygame.time.wait(250)
            draw_window_game_completed(user_text, oigeid)

        # when game end, restart
        if startgame == 2:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if restart_hitbox.collidepoint(mouse_pos):
                        main()
                pygame.time.wait(250)
            draw_window_gameover()


        # hint screen loop
        if startgame == 4:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if jargmine_trashcan_hitbox.collidepoint(mouse_pos):
                        startgame = 1
                        number_question += 1
                        if lives == 0:
                            startgame = 2
                pygame.time.wait(250)
            draw_window_hint( hint)

            # start screen
        if startgame == 0:
            starting_draw_window()
        # when asking questions, game itself
        elif startgame == 1:
            draw_window(lives, user_text, küsimus, oigeid)

if __name__ == "__main__":
    main()