"""Serpente automatico con percorso A* su griglia toroidale."""
import heapq

from config import BLUE
from snake import Snake


class SnakeIA(Snake):
    def __init__(self, x, y, width, height, grid_size=20):
        super().__init__(x, y, width, height, grid_size, BLUE)
        self.direction = (-grid_size, 0)
        self.next_direction = self.direction

    def get_neighbors(self, node):
        x, y = node
        step = self.grid_size
        steps = [(step, 0), (-step, 0), (0, step), (0, -step)]
        return [((x + dx) % self.width, (y + dy) % self.height)
                for dx, dy in steps]

    def heuristic(self, a, b):
        # Distanza di Manhattan con passaggio attraverso i bordi.
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        dx = min(dx, self.width - dx)
        dy = min(dy, self.height - dy)
        return (dx + dy) // self.grid_size

    def find_path(self, start, goal, obstacles):
        queue = [(self.heuristic(start, goal), 0, start)]
        costs = {start: 0}
        came_from = {}
        blocked = set(obstacles)

        while queue:
            _, g, current = heapq.heappop(queue)
            if g != costs.get(current):
                continue  # Voce ormai superata da una strada migliore.
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return list(reversed(path))

            for neighbor in self.get_neighbors(current):
                if neighbor in blocked:
                    continue
                new_cost = g + 1
                if new_cost < costs.get(neighbor, float("inf")):
                    costs[neighbor] = new_cost
                    came_from[neighbor] = current
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(queue, (priority, new_cost, neighbor))
        return []  # Nessun percorso disponibile.

    def choose_direction(self, goal, player_body):
        obstacles = set(player_body) | set(self.body[1:])
        head = self.body[0]
        path = self.find_path(head, goal, obstacles)
        choices = ([path[0]] if path else []) + self.get_neighbors(head)

        for cell in choices:
            if cell in obstacles:
                continue
            dx = (cell[0] - head[0]) % self.width
            dy = (cell[1] - head[1]) % self.height
            if dx == self.grid_size:
                direction = (self.grid_size, 0)
            elif dx == self.width - self.grid_size:
                direction = (-self.grid_size, 0)
            elif dy == self.grid_size:
                direction = (0, self.grid_size)
            else:
                direction = (0, -self.grid_size)
            if len(self.body) > 1 and direction == (
                -self.direction[0], -self.direction[1]
            ):
                continue
            self.change_direction(direction)
            return
        # Se non esiste una strada libera, il movimento successivo
        # potrà terminare la partita: il gioco gestirà la collisione.
