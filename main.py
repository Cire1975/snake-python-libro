"""Gioco classico: Snake contro se stesso."""
import pygame

from config import WIDTH, HEIGHT, GRID_SIZE, FPS, TARGET_SCORE, WHITE, BLACK
from snake import Snake
from apple import Apple


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake classico")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    snake = Snake(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, GRID_SIZE)
    apple = Apple(WIDTH, HEIGHT, GRID_SIZE, snake.body)
    score = 0
    running = True
    playing = True
    final_message = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif playing:
                snake.handle_input(event)

        if not running:
            break

        if playing:
            eaten = snake.next_head() == apple.position
            if eaten:
                snake.grow()
            snake.move()

            if snake.collides_with_self():
                playing = False
                final_message = "Game over: hai toccato il tuo corpo"
            elif eaten:
                score += 1
                if score >= TARGET_SCORE:
                    playing = False
                    final_message = "Hai vinto!"
                elif not apple.respawn(snake.body):
                    playing = False
                    final_message = "Griglia completa: hai vinto!"

        screen.fill(WHITE)
        apple.draw(screen)
        snake.draw(screen)
        score_text = font.render(f"Mele: {score}/{TARGET_SCORE}", True, BLACK)
        screen.blit(score_text, (8, 8))
        if not playing:
            message = font.render(final_message, True, BLACK)
            screen.blit(message, (20, HEIGHT // 2))
            hint = font.render("ESC per uscire", True, BLACK)
            screen.blit(hint, (20, HEIGHT // 2 + 35))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
