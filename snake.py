"""Serpente controllato dalla tastiera o da un joypad compatibile."""
import pygame

from config import GREEN


class Snake:
    def __init__(self, x, y, width, height, grid_size=20, color=GREEN):
        if width % grid_size or height % grid_size:
            raise ValueError("Le dimensioni devono essere multiple della griglia.")
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError("Posizione iniziale fuori dalla finestra.")
        if x % grid_size or y % grid_size:
            raise ValueError("La posizione iniziale deve seguire la griglia.")

        self.body = [(x, y)]
        self.direction = (grid_size, 0)
        self.next_direction = self.direction
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.color = color
        self.grow_next = False

    def change_direction(self, direction):
        step = self.grid_size
        valid = {(step, 0), (-step, 0), (0, step), (0, -step)}
        if direction not in valid:
            return
        opposite = (-self.direction[0], -self.direction[1])
        if len(self.body) > 1 and direction == opposite:
            return
        self.next_direction = direction

    def handle_input(self, event):
        step = self.grid_size
        if event.type == pygame.KEYDOWN:
            keys = {
                pygame.K_UP: (0, -step), pygame.K_w: (0, -step),
                pygame.K_DOWN: (0, step), pygame.K_s: (0, step),
                pygame.K_LEFT: (-step, 0), pygame.K_a: (-step, 0),
                pygame.K_RIGHT: (step, 0), pygame.K_d: (step, 0),
            }
            if event.key in keys:
                self.change_direction(keys[event.key])
        elif event.type == pygame.JOYHATMOTION:
            x, y = event.value
            if x:
                self.change_direction((x * step, 0))
            elif y:
                self.change_direction((0, -y * step))
        elif event.type == pygame.JOYAXISMOTION and abs(event.value) > 0.6:
            if event.axis == 0:
                self.change_direction((step if event.value > 0 else -step, 0))
            elif event.axis == 1:
                self.change_direction((0, step if event.value > 0 else -step))

    def next_head(self):
        x, y = self.body[0]
        dx, dy = self.next_direction
        return ((x + dx) % self.width, (y + dy) % self.height)

    def grow(self):
        self.grow_next = True

    def move(self):
        new_head = self.next_head()
        self.direction = self.next_direction
        self.body.insert(0, new_head)
        if self.grow_next:
            self.grow_next = False
        else:
            self.body.pop()

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        step = self.grid_size
        for x, y in self.body:
            pygame.draw.rect(screen, self.color, (x, y, step, step))
