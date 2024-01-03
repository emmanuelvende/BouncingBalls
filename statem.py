import pygame


class State:
    def __init__(self, context):
        self.context = context

    def idle(self, screen):
        pass

    def click(self, screen):
        pass

    def next_state(self):
        pass


class StateSettingPos(State):
    def idle(self, screen):
        self.context.ball.pos = pygame.mouse.get_pos()
        self.context.ball.draw_body(screen)

    def click(self, screen):
        self.idle(screen)
        self.context.next_state()

    def next_state(self):
        return StateSettingSpeed(self.context)


class StateSettingSpeed(State):
    def idle(self, screen):
        self.context.ball.set_speed(screen, pygame.mouse.get_pos())

    def click(self, screen):
        print(f"yolo on {screen}")


class Context:
    def __init__(self, ball):
        self.ball = ball
        self.state = StateSettingPos(self)

    def idle(self, screen):
        self.state.idle(screen)

    def click(self, screen):
        self.state.click(screen)

    def next_state(self):
        self.state = self.state.next_state()
