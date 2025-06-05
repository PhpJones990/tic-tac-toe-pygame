import pygame

pygame.init()

WINDOW_SIZE = (404, 404)
FPS = 60

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe!")
clock = pygame.time.Clock()

running = True
delta_time = 0.1

images = [
    pygame.image.load("cross.png").convert, 
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

while running:

    screen.fill((0, 0, 0))

    for line in lines:
        pygame.draw.rect(screen, (255, 255, 255), line)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    delta_time = clock.tick(FPS) / 1000
    pygame.display.flip()

pygame.quit()