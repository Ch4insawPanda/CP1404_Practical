from prac_08.Taxi.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi that includes additional costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km*fanciness

    def get_fare(self):
        """Taxi fare multiplied by fanciness with the addition of a flagfall."""
        return (super().get_fare() * self.fanciness) + self.flagfall

    def __str__(self):
        """Redo __str__ to display flagfall."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
