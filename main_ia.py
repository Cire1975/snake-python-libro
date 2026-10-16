"""Sfida: il giocatore e un avversario A* cercano la stessa mela."""
import pygame

from config import WIDTH, HEIGHT, GRID_SIZE, FPS, TARGET_SCORE, WHITE, BLACK
from snake import Snake
from snake_ia import SnakeIA
from apple import Apple


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake contro IA")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    player = Snake(140, 200, WIDTH, HEIGHT, GRID_SIZE)
    ai = SnakeIA(460, 200, WIDTH, HEIGHT, GRID_SIZE)
    apple = Apple(WIDTH, HEIGHT, GRID_SIZE, player.body + ai.body)
    player_score = 0
    ai_score = 0
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
                player.handle_input(event)

        if not running:
            break

        if playing:
            old_player_head, old_ai_head = player.body[0], ai.body[0]
            ai.choose_direction(apple.position, player.body)
            player_eats = player.next_head() == apple.position
            ai_eats = ai.next_head() == apple.position
            if player_eats:
                player.grow()
            if ai_eats:
                ai.grow()
            player.move()
            ai.move()

            crossed = (player.body[0] == old_ai_head and
                       ai.body[0] == old_player_head)
            player_loses = (player.collides_with_self() or
                            player.body[0] in ai.body or crossed)
            ai_loses = (ai.collides_with_self() or
                        ai.body[0] in player.body or crossed)

            if player_loses or ai_loses:
                playing = False
                if player_loses and ai_loses:
                    final_message = "Pareggio: collisione reciproca!"
                elif player_loses:
                    final_message = "Vince lo Snake IA!"
                else:
                    final_message = "Hai vinto: lo Snake IA si e' bloccato!"
            else:
                if player_eats:
                    player_score += 1
                if ai_eats:
                    ai_score += 1
                if player_score >= TARGET_SCORE or ai_score >= TARGET_SCORE:
                    playing = False
                    final_message = ("Hai vinto!" if player_score > ai_score
                                     else "Vince lo Snake IA!")
                elif (player_eats or ai_eats) and not apple.respawn(
                    player.body + ai.body
                ):
                    playing = False
                    final_message = "Griglia completa: partita terminata"

        screen.fill(WHITE)
        apple.draw(screen)
        player.draw(screen)
        ai.draw(screen)
        text = font.render(
            f"Tu: {player_score}    IA: {ai_score}    (primo a {TARGET_SCORE})",
            True, BLACK
        )
        screen.blit(text, (8, 8))
        if not playing:
            text = font.render(final_message, True, BLACK)
            screen.blit(text, (20, HEIGHT // 2))
            hint = font.render("ESC per uscire", True, BLACK)
            screen.blit(hint, (20, HEIGHT // 2 + 35))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
