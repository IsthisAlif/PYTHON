# multiple inheritance   = inherit from more than one parent class
#                          C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleeping(self):
        print(f"{self.name} is sleeping")
class Prey(Animals):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animals):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.flee()
fish.hunt()

rabbit.eat()

hawk.sleep()