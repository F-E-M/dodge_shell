import time


class GameStats:
    def __init__(self):
        self.score = None
        self.tick = time.time()
        self.mg_tick = time.time()

    def reset(self):
        self.score = 0
