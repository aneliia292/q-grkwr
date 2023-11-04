class Soldier:


    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number


def get_rank(self):


    return self.__rank


def confirm_service_number(self, number):


    return self.__service_number == number


def promote(self):

    pass


def demote(self):

    pass

soldier = Soldier("John Doe", "Private", 123456)

print(soldier.name) # Output: John Doe
print(soldier.get_rank()) # Output: Private
print(soldier.confirm_service_number(123456)) # Output: True
print(soldier.confirm_service_number(789012)) # Output: False

soldier.promote()
print(soldier.get_rank()) # Output: New rank after promotion

soldier.demote()
print(soldier.get_rank()) # Output: New rank after demotion
