import pygame

RED = 255, 0, 0

class Ball:
    def __init__(self):
        self.r = 5
        self.pos = 0, 0

    def draw_body(self, surface):
        pygame.draw.circle(surface, RED, self.pos, self.r)