import pygame
import morepygame.arrow
from pygame.math import Vector2 as Vec

# from morepygame.utils import *

RED = 255, 0, 0
YELLOW = 255, 255, 0


class Ball:
    def __init__(self):
        self.r = 5
        self.pos_vec = Vec(0, 0)

    def draw_body(self, surface):
        pygame.draw.circle(surface, RED, self.pos_vec, self.r)

    def set_pos(self, pos):
        self.pos_vec = Vec(pos)

    def draw_speed(self, surface, speed_pos):
        """
        `speed_pos` is pygame (x,y) coordinates of a mouse click to set the speed as
        a vector end, considering the vector start as the already set postiion of the ball.
        """
        pygame.draw.circle(surface, YELLOW, self.pos_vec, self.r)
        morepygame.arrow.draw_arrow(
            surface, start=self.pos_vec, end=speed_pos, width=3, color=YELLOW
        )

    def set_speed(self, speed_pos):
        self.speed_vec = Vec(speed_pos) - Vec(self.pos_vec)

    def move(self, delay):
        self.pos_vec += 0.001 * delay * self.speed_vec
