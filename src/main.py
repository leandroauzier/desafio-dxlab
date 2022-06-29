from board_game.config import settings

from board_game.board.unit import create_board
from board_game.board.statistics import show_statistics

def main():
    results = []
    for i in range(int(settings.ENV_SIMULATIONS)):
        board = create_board()
        while board.winner is None:
            for player in board.players:
                if player.gameover:
                    board.remove(player)
                winner = board.check_winner(player)
                if winner:
                    board.winner = winner
                    break
                board.play(player, board)
            board.played += 1
        results.append(board.finish())
    show_statistics(results)


if __name__ == "__main__":
    main()
