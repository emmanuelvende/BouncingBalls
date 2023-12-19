import pygame
import pygame.draw
import pygame.image
import pygame.mouse
import statem


def main():
    pygame.init()
    decor_surf = pygame.image.load("decor.png")
    w, h = decor_surf.get_width(), decor_surf.get_height()
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    context = statem.Context()

    running = True
    while running:
        screen.blit(decor_surf, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                context.click(screen)

        context.idle(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


main()
