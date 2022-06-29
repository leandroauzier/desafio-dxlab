from .base import BasePlayer


class PlayerCauteloso(BasePlayer):
    def _roles_to_payment(self, patrimony):
        if (self.balance - patrimony.property_price) >= 80:
            self.paid(patrimony.property_price, patrimony.type_of_behaviour)
            return True
        return False
