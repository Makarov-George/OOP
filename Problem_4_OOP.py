import random

class Voin(object):
    def __init__(self, health, armor, endurance):
        self.health = health
        self.armor = armor
        self.end = endurance
    
    def set(self, health, armor, endurance):
        self.health = health
        self.armor = armor
        self.end = endurance

    def get(self):
        return self.health, self.armor, self.end
    
    def hit(self):
        self.end -= 10

    def defence(self):
        self.health -= random.randint(0,20)
        self.armor -= random.randint(0,10)                 

    def fight(self, second_voin):
        def check(self,second_voin):
            kill = ''
            while True:
                if self.health > 10 and second_voin.health > 10:
                    print("У первого воина осталось:",self.health,"хп")
                    print("У второго воина осталось:",second_voin.health,"хп\n")
                    break
                elif self.health > 10 and second_voin.health <= 10:
                    print("У первого воина осталось:",self.health,"хп")
                    while True:
                        kill = input('У второго воина осталось 10 хп, убьем его?(y - убьем, n - пощадим)\n')
                        if kill == 'y':
                            print('Вы убили второго воина\nПервый воин победил!')
                            exit()
                        elif kill == 'n':
                            print('Пощадим его\nПервый воин победил!')
                            exit()
                        else:
                            print('Надо выбрать!!!')
                    break
                elif self.health <= 10 and second_voin.health > 10:
                    print("У второго воина осталось:",second_voin.health,"хп")
                    while kill != 'y' or kill != 'n':
                        kill = input('У первого воина осталось 10 хп, убьем его?(y - убьем, n - пощадим)\n')
                        if kill == 'y':
                            print('Вы убили первого воина\nВторой воин победил!')
                            exit()
                        elif kill == 'n':
                            print('Пощадим его\nВторой воин победил!')
                            exit()
                        else:
                            print('Надо выбрать!!!')
                    break
                else:
                    print("Они убили друг друга(невероятно)")
                    break
        while True:
            r = random.randint(1,4) # 1-Оба атакуют; 2-Первый атакует, второй защищается; 3-Первый защищается, второй атакует; 4-Оба защищаются
            if r == 1:
                print('Оба воина выбрали атаку')
                if self.end > 0 and second_voin.end > 0:
                    self.hit()
                    second_voin.hit()
                    self.health -= random.randint(10,30)
                    second_voin.health -= random.randint(10,30)
                    check(self,second_voin)
                elif self.end > 0 and second_voin.end <= 0:
                    self.hit()
                    self.health -= random.randint(0,10)
                    second_voin.health -= random.randint(10,30)
                    check(self,second_voin)
                elif self.end <= 0 and second_voin.end > 0:
                    second_voin.hit()
                    self.health -= random.randint(10,30)
                    second_voin.health -= random.randint(0,10)
                    check(self,second_voin)
                elif self.end <= 0 and second_voin.end <= 0:
                    self.health -= random.randint(0,10)
                    second_voin.health -= random.randint(0,10)
                    check(self,second_voin)
            elif r == 2:
                print('Первый атакует, второй защищается')
                if self.end > 0 and second_voin.armor > 0:
                    self.hit()
                    second_voin.defence()
                    check(self,second_voin)
                elif self.end > 0 and second_voin.armor <= 0:
                    self.hit()
                    second_voin.health -= random.randint(10,30)
                    check(self,second_voin)
                elif self.end <= 0 and second_voin.armor > 0:
                    second_voin.armor -= random.randint(0,3)
                    second_voin.health -= random.randint(0,7)
                    check(self,second_voin)
                elif self.end <= 0 and second_voin.armor <= 0:
                    second_voin.health -= random.randint(0,10)
                    check(self,second_voin)
            elif r == 3:
                print('Первый защищается, второй атакует')
                if second_voin.end > 0 and self.armor > 0:
                    second_voin.hit()
                    self.defence()
                    check(self,second_voin)
                elif second_voin.end > 0 and self.armor <= 0:
                    second_voin.hit()
                    self.health -= random.randint(10,30)
                    check(self,second_voin)
                elif second_voin.end <= 0 and self.armor > 0:
                    self.armor -= random.randint(0,3)
                    self.health -= random.randint(0,7)
                    check(self,second_voin)
                elif second_voin.end <= 0 and self.armor <= 0:
                    self.health -= random.randint(0,10)
                    check(self,second_voin)
            else:
                print('Оба защищаются\n')


voin_1 = Voin(100,50,50)
voin_2 = Voin(100,50,50)
voin_1.fight(voin_2)  
