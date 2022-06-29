from .base import BasePlayer


class PlayerImpulsivo(BasePlayer):
    def _roles_to_payment(self, patrimony):
        self.paid(patrimony.property_price, patrimony.type_of_behaviour)
        return True
