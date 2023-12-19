import pygame.mouse


class State:
    def __init__(self, context):
        self.context = context

    def idle(self, screen):
        pass

    def click(self, screen):
        pass

    def get_next_state(self):
        pass


class PrepareBallPosState(State):
    def idle(self, screen):
        RED = 255, 0, 0
        w, h = screen.get_size()
        r = (w**2 + h**2) ** 0.5 / 100
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, RED, (x, y), r)

    def click(self, screen):
        self.context.transition_to_next_state()

    def get_next_state(self):
        return PrepareBallSpeedState(self.context)


class PrepareBallSpeedState(State):
    def idle(self, screen):
        YELLOW = (255, 255, 0)
        w, h = screen.get_size()
        r = (w**2 + h**2) ** 0.5 / 100
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, YELLOW, (x, y), r)

    def click(self, screen):
        print(f"yolo on {screen}")



class Context:
    def __init__(self):
        self.state = PrepareBallPosState(self)

    def idle(self, screen):
        self.state.idle(screen)

    def click(self, screen):
        self.state.click(screen)

    def go_to_next_state(self):
        self.state = self.state.get_next_state()
