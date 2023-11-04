class Recipe:
    def __init__(self, name, ing):
        self.name = name
        self.ing = ing
    def print_ing(self):
        print(f'Ингредиенты для {self.name}')
        for i in self.ing:
            print('-', i)
    def cook(self):
        print(f'Сегодня мы готовим {self.name}.\nВыполняем инструкцию по приготовлению блюда {self.name}.\nБлюдо Спагетти болоньезе готово!):
spaghetti = Recipe('Спагетти болоньезе', 'Спагетти', 'Фарш', 'Томатный соус', 'Лук', 'Чеснок', 'Соль')
