"""Generazione di una mela soltanto su celle libere."""
import random
import pygame

from config import RED


class Apple:
    def __init__(self, width, height, grid_size=20, occupied=()):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.position = None
        self.respawn(occupied)

    def respawn(self, occupied):
        blocked = set(occupied)
        free = [
            (x, y)
            for x in range(0, self.width, self.grid_size)
            for y in range(0, self.height, self.grid_size)
            if (x, y) not in blocked
        ]
        self.position = random.choice(free) if free else None
        return self.position is not None

    def draw(self, screen):
        if self.position is not None:
            x, y = self.position
            pygame.draw.rect(
                screen, RED, (x, y, self.grid_size, self.grid_size)
            )
