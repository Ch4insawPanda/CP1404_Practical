class Guitar:

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return'{} ({}) : ${:.2f}'.format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of the guitar."""
        return 2021-self.year

    def is_vintage(self):
        """Check to see if the guitar is a vintage."""
        return self.get_age() >= 50
