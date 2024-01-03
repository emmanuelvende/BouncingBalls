import pygame
import morepygame.arrow

RED = 255, 0, 0
YELLOW = 255, 255, 0


class Ball:
    def __init__(self):
        self.r = 5
        self.pos = 0, 0

    def draw_body(self, surface):
        pygame.draw.circle(surface, RED, self.pos, self.r)

    def set_speed(self, surface, speed_pos):
        """
        `speed_pos` is pygame (x,y) coordinates of a mouse click to set the speed as
        a vector end, considering the vector start as the already set postiion of the ball.
        """
        pygame.draw.circle(surface, YELLOW, self.pos, self.r)
        morepygame.arrow.draw_arrow(
            surface, start=self.pos, end=speed_pos, width=3, color=YELLOW
        )
