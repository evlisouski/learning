from collections import namedtuple

hero_1 = ('Azz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])

class Person:

    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght

hero_2 = Person("Azz", "Izverg", 100, 0.0, 250)
print(hero_2.mana)

New_Person = namedtuple('New_Person', 'name, race, health, mana, strenght')
hero_3 = New_Person("Aaz", 'Izverg', 100, 0.0, 250)
print(hero_3.race)
