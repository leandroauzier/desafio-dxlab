from abc import ABC, abstractmethod
from board_game.config import settings


class BasePlayer(ABC):

    def __init__(
        self, behaviour, position=0,
        balance=settings.ENV_BALANCE
    ):
        self.position = position
        self.balance = balance
        self.behaviour = behaviour
        self.gameover = False

    def __str__(self):
        return f"{self.behaviour}"

    def __repr__(self):
        return f"{self.behaviour}"

    def income_or_sale(self, patrimony, board=None):
        if patrimony.type_of_behaviour:
            if self != patrimony.type_of_behaviour:
                self.paid(patrimony.rental_price, patrimony.type_of_behaviour)
            return

        if self._roles_to_payment(patrimony):
            patrimony.type_of_behaviour = self

    @abstractmethod
    def _roles_to_payment(self, patrimony, board):
        raise NotImplementedError()

    def paid(self, property_price, type_of_behaviour=None):
        self.balance -= property_price
        if type_of_behaviour:
            type_of_behaviour.balance += property_price
        if not self.balance:
            self.gameover = True
