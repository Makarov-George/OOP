import random

class Voin(object):
    def __init__(self, health):
        self.health = health
    
    def set_health(self, health):
        self.health = health
    
    def get(self):
        return self.health
    
    def hit(self):
        self.health -= 20
    
    def fight(self, second_fighter):
        while True:
            r = random.randint(1,2)
            if r == 1:
                print('Первый воин атакует!')
                second_fighter.hit()
                if second_fighter.get() > 0:
                    print("У второго воина осталось:",second_fighter.get(),"хп\n")
                else:
                    print("У второго воина не осталось здоровья\nПервый воин победил!")
                    break
            else:
                print('Второй воин атакует!')
                self.hit()
                if self.get() > 0:
                    print("У первого воина осталось:",self.get(),"хп\n")
                else:
                    print("У первого воина не осталось здоровья\nВторой воин победил!")
                    break
voin_1 = Voin(100)
voin_2 = Voin(100)
voin_1.fight(voin_2)
