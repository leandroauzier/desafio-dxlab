from random import randint
from .base import BasePlayer


class PlayerAleatorio(BasePlayer):
    def _roles_to_payment(self, patrimony):
        if randint(0, 1) > 0:
            self.paid(patrimony.property_price, patrimony.type_of_behaviour)
            return True
        return False
