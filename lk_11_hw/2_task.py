class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.__friends = []

    def know(self, other):
        self.__friends.append(other)

    def is_known(self, other):
        return other in self.__friends


person1 = Person(18, 'Oleg')
person2 = Person(24, 'Dima')
person3 = Person(25, 'Vitalik')
person1.know(person2)
print(person1.is_known(person2))
print(person1.is_known(person3))


