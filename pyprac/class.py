# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point = Point(10, 20)
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
#     def name(self):
#         print("name")
#     def talk(self):
#         print(f"Hi, I am {self.name}")
# ali = Person("Ali")
#
# ali.talk()
# ahsan = Person("Ahsan")
# ahsan.talk()


# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
# cat1 = Cat()
# cat1.be_annoying()
class Family:
    def __init__(self, mother="Aaba", father="Aata", children=()):
        self.mother = mother
        self.father = father
        self.children = children
        return

    def activities(self):
        print("eat, drink, walk, work")

    def hasChildren(self):
        print(len(self.children) > 0)

    def headOfFamily(self):
        return self.mother

#
# class Family(human):
#     @staticmethod
#     def females():
#         print("height: medium, weight: overweight,")
#     @staticmethod
#     def males():
#         print("height: Tall, weight: Normal, ")
#
# class Children(Family):
#     def female_children(self):
#         print("cute, hard_working, study ")
#     def male_children(self):
#         print("annoying, lazy, messy")

maqsoodi = Family(mother="anissa", father="Ata Jan", children=("Ali", "Simin", "Mohadesa"))

nazer = Family(mother="Amina", father="Ewaz", children=("Ahsan", "Asad"))

defaultFamily = Family()

# anisa = Family()
# anisa.activities()
# anisa.females()
# aqayee_sharifi = Family()
# aqayee_sharifi.males()
# aqayee_sharifi.activities()
# ali = Children()
# ali.male_children()
# simin = Children()
# simin.female_children()
# simin.activities()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def printCard(self):
        print(self.suit, self.rank)
    def __str__(self):
        return self.suit + " " + str(self.rank)

card1 = Card("spades", 4)
card2 = Card("hearts", 12)
print(card1.printCard())
print(card1)

#print(card2.printCard())

class Deck:
    def __init__(self):
        self.l = []
        for i in range(1, 11):
            self.l.append(Card("spades", i))
    def printDeck(self):
        for i in self.l:
            print(i)
print("I am creating a deck.")
deck1 = Deck()
print(deck1.printDeck())

class Deck:
    def __init__(self):
        self.l = []
        for i in range(1, 11):
            self.l.append(Card(suit, i))
            



print("I am learning about classes")







