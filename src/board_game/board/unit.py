from board_game.config import settings

from .game_board import GameBoard
from .player_cauteloso import PlayerCauteloso
from .player_exigente import PlayerExigente
from .player_impulsivo import PlayerImpulsivo
from .player_aleatorio import PlayerAleatorio

behaviours = {
    "impulsivo": PlayerImpulsivo,
    "exigente": PlayerExigente,
    "cauteloso": PlayerCauteloso,
    "aleatorio": PlayerAleatorio
}


def create_player(behaviour: str, *args, **kwargs):
    try:
        return behaviours[behaviour](behaviour=behaviour, *args, **kwargs)

    except KeyError:
        available_behaviours = ", ".join(behaviours.keys())
        raise NotImplementedError(
            f"O comportamento do player '{behaviour}' não foi implementado."
            f"Por favor use os comportamentos disponíveis: {available_behaviours}"
        )


def create_board():
    board = GameBoard()
    players = [
        create_player(behaviour)
        for behaviour in settings.ENV_BEHAVIOUR
    ]
    board.players = players
    return board
