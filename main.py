import pygame

# initialize pygame and some values 
pygame.init()

WINDOW_SIZE = (404, 404)
FPS = 60

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe!")
clock = pygame.time.Clock()

# player 1 Win menu
def player_1_win():
    running = True

    font = pygame.font.Font(None, size=50)

    while running:

        screen.fill((0, 0, 0))

        text = font.render("Player 1 Wins!", True, (255, 255, 255))
        screen.blit(text, (85, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

# player 2 Win menu
def player_2_win():
    running = True
    
    font = pygame.font.Font(None, size=50)
    
    while running:
    
        screen.fill((0, 0, 0))
    
        text = font.render("Player 2 Wins!", True, (255, 255, 255))
        screen.blit(text, (85, 160))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    
        pygame.display.flip()
        clock.tick(FPS)

# Draw menu
def draw():
    running = True
    
    font = pygame.font.Font(None, size=50)
    
    while running:
    
        screen.fill((0, 0, 0))
    
        text = font.render("Draw!", True, (255, 255, 255))
        screen.blit(text, (150, 160))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    
        pygame.display.flip()
        clock.tick(FPS)

# main game menu
def game_menu():

    # load some values
    running = True

    images = [
        pygame.image.load("cross.png").convert(), 
        pygame.image.load("circle.png").convert()
            ]

    for image in images:
        image.set_colorkey((0, 0, 0))

    lines = [
        pygame.Rect(128, 0, 10, 404), 
        pygame.Rect(266, 0, 10, 404),
        pygame.Rect(0, 128, 404, 10),
        pygame.Rect(0, 266, 404, 10)
            ]

    squares = [
        [pygame.Rect(0, 0, 128, 128), pygame.Rect(138, 0, 128, 128), pygame.Rect(276, 0, 128, 128)],
        [pygame.Rect(0, 138, 128, 128), pygame.Rect(138, 138, 128, 128), pygame.Rect(276, 138, 128, 128)],
        [pygame.Rect(0, 276, 128, 128), pygame.Rect(138, 276, 128, 128), pygame.Rect(276, 276, 128, 128)]
        ]

    board = [
        [0, 0, 0],    #[0][0]    [0][1]     [0][2]
        [0, 0, 0],    #[1][0]    [1][1]     [1][2]
        [0, 0, 0]     #[2][0]    [2][1]     [2][2]
            ]

    board_bool = [
        [False, False, False],    #[0][0]    [0][1]     [0][2]
        [False, False, False],    #[1][0]    [1][1]     [1][2]
        [False, False, False]     #[2][0]    [2][1]     [2][2]
            ]

    player_turn = 1

    def check_win(board):

        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] and row[0] in [1, 2]:
                return row[0]

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] in [1, 2]:
                return board[0][col]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] in [1, 2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] in [1, 2]:
            return board[0][2]

        # No winner found
        is_draw = True
        for row in board:
            for cell in row:
                if cell not in [1, 2]:  # If any cell is empty
                    is_draw = False
                    break
            if not is_draw:
                break
            
        return 0 if is_draw else None

    # main game loop
    while running:

        screen.fill((0, 0, 0))

        # Draw the lines
        for line in lines:
            pygame.draw.rect(screen, (255, 255, 255), line)

        m_pos = pygame.mouse.get_pos()
        m_pressed = pygame.mouse.get_pressed()

        # check the squares and mark the squares states with player 1 or 2
        y = 0
        for row in squares:
            x = 0
            for square in row:
                if square.collidepoint(m_pos) and m_pressed[0]:
                    if player_turn == 1:
                        if not board_bool[y][x] and board_bool[y][x] == 0:
                            board_bool[y][x] = True
                            board[y][x] = 1
                            player_turn = 2
                    elif player_turn == 2:
                        if not board_bool[y][x] and board_bool[y][x] == 0:
                            board_bool[y][x] = True
                            board[y][x] = 2
                            player_turn = 1
                x += 1
            y += 1

        # Draw the squares according to the board state
        y = 0
        for row in squares:
            x = 0
            for square in row:
                if board_bool[y][x] and board[y][x] == 1:
                    screen.blit(images[0], square)
                if board_bool[y][x] and board[y][x] == 2:
                    screen.blit(images[1], square)
                x += 1
            y += 1

        # check the game conditions
        if check_win(board) == 1:
            running = False
            player_1_win()
        elif check_win(board) == 2:
            running = False
            player_2_win()
        elif check_win(board) == 0:
            running = False
            draw()

        # take user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

# main menu
def main_menu():

    # load some values
    running = True

    font0 = pygame.font.Font(None, size=50)
    font1 = pygame.font.Font(None, size=100)
    font2 = pygame.font.Font(None, size=25)
    button = pygame.Rect(102, 152, 200, 100)

    # main game loop
    while running:

        screen.fill((0, 0, 0))

        # draw the texts
        title_text = font0.render("Tic Tac Toe!", True, (255, 255, 255))
        screen.blit(title_text, (105, 50))

        pygame.draw.rect(screen, (255, 255, 255), button)
        start_text = font1.render("Start", True, (0, 0, 0))
        screen.blit(start_text, (122, 170))

        name_text = font2.render("Made by PhpJones", True, (255, 255, 255))
        screen.blit(name_text, (125, 350))

        # m_pos = pygame.mouse.get_pos()
        # m_pressed = pygame.mouse.get_pressed()

        # if button.collidepoint(m_pos) and m_pressed[0]:
        #     running = False
        #     game_menu()

        # take user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    running = False
                    game_menu()

        pygame.display.flip()
        clock.tick(FPS)

main_menu()

pygame.quit()