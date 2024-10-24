class Anumal:
    alive = True
    fed = False
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        if food.edible:
            print(f'{self.name},cъел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False
    def __init__(self,name):
        self.name = name


class Mammal(Anumal):
    pass

class Predator(Anumal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self,name):
        super().__init__(name)
        self.edible = True

a1 = Predator('лев')
a2 = Mammal('бык')
p1 = Flower('крапива')
p2 =Fruit('манго')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


