import pygame
import statem
import ball

def main():
    pygame.init()
    decor_surf = pygame.image.load("decor.png")
    w, h = decor_surf.get_width(), decor_surf.get_height()
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()


    the_ball = ball.Ball()
    context = statem.Context(the_ball)

    running = True
    tick_delay = 0.0
    while running:
        screen.blit(decor_surf, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                context.click(screen)

        context.idle(screen, tick_delay)

        pygame.display.flip()

        tick_delay = clock.tick(60)

    pygame.quit()


main()
