import pygame
import os
from pygame.locals import *
from questions import *
from random import randint
import pygame.freetype
import sqlite3


# Sqllite cur
uhendus = sqlite3.connect('assets/score.db')
c = uhendus.cursor()


# Pygame starts here
pygame.font.init()


# Define general info
WIDTH, HEIGHT = 1200, 630
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorteerimine")
pygame.display.set_icon(pygame.image.load("assets/trashcan.png"))
FPS = 200


# Game stage
startgame = 0


# Define colors
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
TRASHCAN_TEXT_COLOR = (255, 255, 255)
QUESTION_TEXT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)


# Import fonts
pygame.freetype.init()

# Define fonts
HEALTH_FONT = pygame.font.Font('assets/dogicapixel.ttf', 25)
PLAYER_TEXT_FONT = pygame.font.Font('assets/dogicapixel.ttf', 25)
START_GAME_FONT = pygame.font.Font('assets/dogicapixel.ttf', 80)
BASE_FONT = pygame.font.Font('assets/dogicapixel.ttf', 30) # user text
TRASHCAN_FONT = pygame.font.Font('assets/dogicapixel.ttf',20)
QUESTION_FONT = pygame.font.Font('assets/dogicapixel.ttf', 30)


# Input field info
user_text = ''
input_rect = pygame.Rect(525, 290, 140, 40)
input_rect_box = pygame.draw.rect(SCREEN, GREY, input_rect)


# Start game label
start_game_text = START_GAME_FONT.render("START GAME", True, WHITE)
START_GAME_BOX = pygame.Rect((WIDTH - start_game_text.get_width()) // 2, (HEIGHT - start_game_text.get_height()) // 2-105, start_game_text.get_width(), start_game_text.get_height()+10)
# Start game hitbox
startgamebox = pygame.draw.rect(SCREEN, GREY, START_GAME_BOX)


# Define the background
# Main background
loop_bg = pygame.image.load('assets/loop3.png')
bg = pygame.transform.scale(loop_bg, (1200, 630))
# Start screen, game end screens
loop2_bg = pygame.image.load('assets/retro.png')
bg2 = pygame.transform.scale(loop2_bg, (1200, 630))

# Load life images
three_lives = pygame.image.load('assets/3elu.png')
two_lives = pygame.image.load('assets/2elu.png')
one_life = pygame.image.load('assets/1elu.png')


# Define the trashcan
TRASHWIDTH, TRASHHEIGHT = 200, 200
TRASHCAN_IMAGE = pygame.image.load(os.path.join('assets/trashcan.png'))
TRASHCAN = pygame.transform.scale(TRASHCAN_IMAGE, (TRASHWIDTH, TRASHHEIGHT))


# HITBOXES -----------------------------------------------------------------------------------

# METALL JA PLASTIK
trashcan_box = pygame.Rect(50, 610 - TRASHCAN.get_height() + 20, 120, 160)
metall_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# OHTLIKUDJÄÄTMED
trashcan_box = pygame.Rect(195, 610 - TRASHCAN.get_height() + 20, 120, 160)
ohtlik_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# BIOJÄÄTMED
trashcan_box = pygame.Rect(340, 610 - TRASHCAN.get_height() + 20, 120, 160)
bio_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# PAPP JA PABER
trashcan_box = pygame.Rect(475, 610 - TRASHCAN.get_height() + 20, 120, 160)
papp_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# KLAAS
trashcan_box = pygame.Rect(617, 610 - TRASHCAN.get_height() + 20, 120, 160)
klaas_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# OLMEPRÜGI
trashcan_box = pygame.Rect(755, 610 - TRASHCAN.get_height() + 20, 120, 160)
olme_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# JÄÄTMEJAAM
trashcan_box = pygame.Rect(895, 610 - TRASHCAN.get_height() + 20, 120, 160)
jaatmejaam_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# RIIDE KONTEINER
trashcan_box = pygame.Rect(1035, 610 - TRASHCAN.get_height() + 20, 120, 160)
riide_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# JÄRGMINE ESE BUTTON
trashcan_box = pygame.Rect(540, 610 - TRASHCAN.get_height() - 140, 120, 160)
jargmine_trashcan_hitbox = pygame.draw.rect(SCREEN, GREY, trashcan_box)

# RESTART GAME BUTTON
restart_box = pygame.Rect((WIDTH - 450) // 2, (HEIGHT - 135) // 2, 490, 85)
restart_hitbox = pygame.draw.rect(SCREEN, GREY, restart_box)

# HITBOXES ------------------------------------------------------------------------------------


# Define color change speed and dir
col_spd = 1
col_dir = [0, 1, 0]
def_col = [255, 1, 0]
def_col2 = [70, 250, 120]

# Set the min and max of RGB
minimum = 0
maximum = 255

# Set index for color change
i = 0
# Set index for moving background
x = 0

# Mouse mech shit
y = 1
z = 0

# Color change func
def color_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= maximum or col[i] <= minimum:
            dir[i] *= -1


# Starting screen
def starting_draw_window():
    global x

    # Moving background
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bg2, (x, 0))
    SCREEN.blit(bg2, (WIDTH + x, 0))

    if x == -WIDTH:
        SCREEN.blit(bg2, (WIDTH + x, 0))
        x = 0

    x -= 1


    # Draw start game box
    startgamebox = pygame.draw.rect(SCREEN, def_col2, START_GAME_BOX,2)
    my_font = pygame.font.Font('assets/dogicapixel.ttf', 80)
    text_image = my_font.render("START GAME", True, def_col2)
    SCREEN.blit(text_image, ((WIDTH - text_image.get_width()) // 2, (HEIGHT - text_image.get_height()) // 2 - 100))


    # Draw user input box
    pygame.draw.rect(SCREEN, def_col2, input_rect, 2, 15)
    text_surface = BASE_FONT.render(user_text, True, def_col2)
    SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 6))
    input_rect.w = max(150, text_surface.get_width() + 10)

    # Color change func
    color_change(def_col2, col_dir)


    pygame.display.update()


# Main screen
def draw_window(lives, user_text, küsimus, oigeid):
    global x

    # Moving background
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bg, (x, 0))
    SCREEN.blit(bg, (WIDTH + x, 0))

    if x == -WIDTH:
        SCREEN.blit(bg, (WIDTH + x, 0))
        x = 0

    x -= 1


    # Health, name, points drawing
    if lives == 3:
        SCREEN.blit(three_lives, (1010, 105 - three_lives.get_height()))
    elif lives == 2:
        SCREEN.blit(two_lives, (1010, 105 - two_lives.get_height()))
    elif lives == 1:
        SCREEN.blit(one_life, (1010, 105 - one_life.get_height()))

    user_text = HEALTH_FONT.render("Nimi: " + str(user_text), True, WHITE)
    SCREEN.blit(user_text, (WIDTH - user_text.get_width() - 10, 20))

    oigeid = HEALTH_FONT.render("Punktid: " + str(oigeid), True, WHITE)
    SCREEN.blit(oigeid, (WIDTH - oigeid.get_width() - 10, 100))


    # TRASHCANS --------------------------------------------------------------------------

    # METALL JA PLASTIK CAN
    SCREEN.blit(TRASHCAN, (10, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Metall ja", True, WHITE)
    SCREEN.blit(trashcan_text, (40, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("plastik", True, WHITE)
    SCREEN.blit(trashcan_text, (55, 610 - TRASHCAN.get_height()+ 100))


    # OHTLIKUD JÄÄTMED CAN
    SCREEN.blit(TRASHCAN, (155, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Ohtlikud", True, WHITE)
    SCREEN.blit(trashcan_text, (195, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jäätmed", True, WHITE)
    SCREEN.blit(trashcan_text, (200, 610 - TRASHCAN.get_height() + 100))


    # BIOJÄÄTMED CAN
    SCREEN.blit(TRASHCAN, (295, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Bio-", True, WHITE)
    SCREEN.blit(trashcan_text, (370, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jäätmed", True, WHITE)
    SCREEN.blit(trashcan_text, (340, 610 - TRASHCAN.get_height() + 100))


    # PAPP JA PABER CAN
    SCREEN.blit(TRASHCAN, (435, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Papp ja ", True, WHITE)
    SCREEN.blit(trashcan_text, (483, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("paber", True, WHITE)
    SCREEN.blit(trashcan_text, (495, 610 - TRASHCAN.get_height() + 100))


    # KLAAS CAN
    SCREEN.blit(TRASHCAN, (575, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Klaas", True, WHITE)
    SCREEN.blit(trashcan_text, (635, 610 - TRASHCAN.get_height() + 85))


    # OLMEJÄÄTMED CAN
    SCREEN.blit(TRASHCAN, (715, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Olme-", True, WHITE)
    SCREEN.blit(trashcan_text, (775, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jäätmed", True, WHITE)
    SCREEN.blit(trashcan_text, (760, 610 - TRASHCAN.get_height() + 100))


    # JÄÄTMEJAAM
    SCREEN.blit(TRASHCAN, (855, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Jäätme-", True, WHITE)
    SCREEN.blit(trashcan_text, (900, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("jaam", True, WHITE)
    SCREEN.blit(trashcan_text, (920, 610 - TRASHCAN.get_height() + 100))


    # RIIDE KONTEINER
    SCREEN.blit(TRASHCAN, (995, 610 - TRASHCAN.get_height()))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Riide-", True, WHITE)
    SCREEN.blit(trashcan_text, (1055, 610 - TRASHCAN.get_height() + 70))
    trashcan_text = TRASHCAN_FONT.render("konteiner", True, WHITE)
    SCREEN.blit(trashcan_text, (1030, 610 - TRASHCAN.get_height() + 100))

    # -------------------------------------------------------------------------------------

    # QUESTION
    main_question_text = QUESTION_FONT.render(str(küsimus), True, WHITE)
    SCREEN.blit(main_question_text, (50, 60))


    pygame.display.update()


# Wrong answer screen
def draw_window_hint(hint):
    global x

    # Moving background
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bg, (x, 0))
    SCREEN.blit(bg, (WIDTH + x, 0))

    if x == -WIDTH:
        SCREEN.blit(bg, (WIDTH + x, 0))
        x = 0

    x -= 1


    # Hint text
    main_hint_text = QUESTION_FONT.render(hint, True, WHITE)
    SCREEN.blit(main_hint_text, (50, 200))

    # Next item can and hitbox
    SCREEN.blit(TRASHCAN, (500, 610 - TRASHCAN.get_height() - 160 ))
    # TEXT
    trashcan_text = TRASHCAN_FONT.render("Järgmine ese", True, WHITE)
    SCREEN.blit(trashcan_text, (500, 610 - TRASHCAN.get_height()-60 ))


    pygame.display.update()


# Game failed screen
def draw_window_gameover():
    global x

    # Moving background
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bg2, (x, 0))
    SCREEN.blit(bg2, (WIDTH + x, 0))

    if x == -WIDTH:
        SCREEN.blit(bg2, (WIDTH + x, 0))
        x = 0

    x -= 1


    # Game over label
    game_over_text = START_GAME_FONT.render("GAME OVER", True, def_col2)
    SCREEN.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, (HEIGHT-300) // 2 ))

    # Restart button and hitbox
    restart_text = START_GAME_FONT.render("RESTART", True, def_col2)
    SCREEN.blit(restart_text, ((WIDTH - 450) // 2, (HEIGHT - 120) // 2))
    pygame.draw.rect(SCREEN, def_col2, restart_hitbox, 2)

    # Color change func
    color_change(def_col2, col_dir)


    pygame.display.update()


# Game completed screen
def draw_window_game_completed(user_text, oigeid):
    global x

    # Moving background
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bg2, (x, 0))
    SCREEN.blit(bg2, (WIDTH + x, 0))

    if x == -WIDTH:
        SCREEN.blit(bg2, (WIDTH + x, 0))
        x = 0

    x -= 1


    # Ending scores, info
    game_completed_text = PLAYER_TEXT_FONT.render(str(user_text) + " läbis mängu " + str(oigeid) + " punktiga", True, def_col2)
    SCREEN.blit(game_completed_text, ((WIDTH - game_completed_text.get_width())// 2, (HEIGHT - 250) // 2))

    # Game completed label
    game_over_text = START_GAME_FONT.render("GAME COMPLETED", True, def_col2)
    SCREEN.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, (HEIGHT - 450) // 2))

    # Restart button and hitbox
    restart_text = START_GAME_FONT.render("RESTART", True, def_col2)
    SCREEN.blit(restart_text, ((WIDTH - 450) // 2, (HEIGHT - 120) // 2))
    pygame.draw.rect(SCREEN, def_col2, restart_hitbox, 2)

    # color change func
    color_change(def_col2, col_dir)


    pygame.display.update()


# Activity
active = False
# main func
def main():
    global user_text
    global active
    global y
    global z

    # Lists
    kusimused_list = [question1.question, question2.question, question3.question, question4.question, question5.question, question6.question, question7.question, question8.question, question9.question, question10.question, question11.question, question12.question, question13.question, question14.question, question15.question, question16.question, question17.question, question18.question, question19.question, question20.question]
    oiged_list = [question1.right_answer, question2.right_answer, question3.right_answer, question4.right_answer, question5.right_answer, question6.right_answer, question7.right_answer, question8.right_answer, question9.right_answer, question10.right_answer, question11.right_answer, question12.right_answer, question13.right_answer, question14.right_answer, question15.right_answer, question16.right_answer, question17.right_answer, question18.right_answer, question19.right_answer, question20.right_answer]
    hint_list = [question1.hint, question2.hint, question3.hint, question4.hint, question5.hint, question6.hint, question7.hint, question8.hint, question9.hint, question10.hint, question11.hint, question12.hint, question13.hint, question14.hint, question15.hint, question16.hint, question17.hint, question18.hint, question19.hint, question20.hint]
    koik_kusimused = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20]

    # Randomise lists
    randomized_questions_list = []
    randomized_answers_list = []
    randomized_hint_list = []

    # Asking questions loop and hints
    for i in koik_kusimused:
        randomnumber = randint(0, len(kusimused_list) - 1)
        randomized_questions_list.append(kusimused_list[randomnumber])
        randomized_answers_list.append(oiged_list[randomnumber])
        randomized_hint_list.append(hint_list[randomnumber])

        # Delete the already asked ones
        del kusimused_list[randomnumber]
        del oiged_list[randomnumber]
        del hint_list[randomnumber]


    # Define some vars
    startgame = 0
    lives = 3
    oigeid = 0
    number_question = 0

    # Set delay
    clock = pygame.time.Clock()

    # Game status
    run = True
    # Game logic
    while run:

        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Set frames
        clock.tick(FPS)

        # Mouse mech for stupid reasons
        if y == 0:
            z += 1

        for event in pygame.event.get():
            if z >= 10:
                y = 1
                z = 0
            if event.type == pygame.QUIT:
                run = False
                # If exit game, close database
                c.close()
                pygame.quit()

            # If start screen , select/deselect input field
            if startgame == 0:
                if event.type == pygame.MOUSEBUTTONUP:
                    if input_rect_box.collidepoint(mouse_pos):
                        active = True
                    else:
                        active = False

            # Start screen user input field delete
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

            # Press on start screen
            if startgame == 0:
                if event.type == MOUSEBUTTONUP and y == 1:
                    y = 0
                    if event.button == 1:
                        if startgamebox.collidepoint(mouse_pos):
                            startgame = 1

        # Main screen, asking questions
        if startgame == 1:
            if number_question == number_question:
                hint = randomized_hint_list[number_question]
                küsimus = randomized_questions_list[number_question]
            # Stupid mouse mech
            if event.type == MOUSEBUTTONUP and y == 1:
                y = 0
                if event.button == 1:

                    # Trashcan clicks, ask which trashcan and if correct, life logic ----------------------------------
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
                #sleep
                    # -------------------------------------------------------------------------------------------------


        # If all questions are asked, end screen
        if number_question == len(koik_kusimused):
            startgame = 3

        # When game end, restart (GAME COMPLETED)
        if startgame == 3:
            # If the restart screen comes, save to db
            c.execute("SELECT name, punktid from scoreboard WHERE name=?", [user_text])
            result = c.fetchone()
            if result:
                c.execute("UPDATE scoreboard SET punktid=? WHERE name=?", (oigeid, user_text))
            else:
                c.execute("insert into scoreboard (name, punktid) values (?, ?)", (user_text, oigeid))

            uhendus.commit()

            # If press restart go to start screen
            if event.type == MOUSEBUTTONUP and y == 1:
                y = 0
                if event.button == 1:

                    if restart_hitbox.collidepoint(mouse_pos):
                        main()
                # sleep
            draw_window_game_completed(user_text, oigeid)

        # When game end, restart (GAME OVER)
        if startgame == 2:
            # If the restart screen comes, save to db
            c.execute("SELECT name, punktid from scoreboard WHERE name=?", [user_text])
            result = c.fetchone()
            if result:
                c.execute("UPDATE scoreboard SET punktid=? WHERE name=?", (oigeid, user_text))
            else:
                c.execute("insert into scoreboard (name, punktid) values (?, ?)", (user_text, oigeid))

            uhendus.commit()

            # If press restart go to start screen
            if event.type == MOUSEBUTTONUP and y == 1:
                y = 0
                if event.button == 1:
                    if restart_hitbox.collidepoint(mouse_pos):
                        main()
            draw_window_gameover()


        # Hint screen
        if startgame == 4:
            if event.type == MOUSEBUTTONUP and y == 1:
                y = 0
                if event.button == 1:

                    if jargmine_trashcan_hitbox.collidepoint(mouse_pos):
                        startgame = 1
                        number_question += 1
                        if lives == 0:
                            startgame = 2
                # sleep
            draw_window_hint(hint)

        # Start screen
        if startgame == 0:
            starting_draw_window()
        # When asking questions, game itself
        elif startgame == 1:
            draw_window(lives, user_text, küsimus, oigeid)

if __name__ == "__main__":
    main()
