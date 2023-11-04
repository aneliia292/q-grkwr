class Recipe:


    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


def print_ingredients(self):


    print (f"Ingredients for {self.name}:")
for ingredient in self.ingredients:
    print (ingredient)


def cook(self):


    print (f"Recipe: {self.name}")
print ("Cooking...")
print ("Done!")

recipe = Recipe ("Spaghetti Carbonara", ["Spaghetti", "Eggs", "Bacon", "Parmesan cheese", "Black pepper", "Olive oil"])

recipe.print_ingredients ()
print ()
recipe.cook ()
