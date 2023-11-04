class Candy:

    def __init__(self, name, price, weight):

        self.name = name
        self.price = price
        self.weight = weight


class Chocolate (Candy):

    def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):

        super ().__init__ (name, price, weight)
        self.cocoa_percentage = cocoa_percentage
        self.chocolate_type = chocolate_type


class Gummy (Candy):

    def __init__(self, name, price, weight, flavor, shape):

        super ().__init__ (name, price, weight)

        self.flavor = flavor
        self.shape = shape


class HardCandy (Candy):

    def __init__(self, name, price, weight, flavor, filled):

        super ().__init__ (name, price, weight)
        self.flavor = flavor
        self.filled = filled

        chocolate = Chocolate ("Milka", 2.99, 100, 70, "dark")
        gummy = Gummy ("Haribo", 1.5, 50, "strawberry", "bear")
        hard_candy = HardCandy ("Jolly Rancher", 0.99, 10, "watermelon", True)
