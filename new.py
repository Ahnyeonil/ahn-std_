from animal import dog
from animal import cat

from animal import *

fruit = ["사과", "사과", "바나나", "바나나", "바나나", "딸기", "키위", "포도", "포도", "포도", "포도", "포도", "복숭아"]

dic = {}

for f in fruit:
    if f in dic:
        dic[f] = dic[f] + 1
    else:
        dic[f] = 1

print(dic)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_h(self, to_name):
        print("Hello! " + to_name + ", My name is " + self.name)

    def intro(self):
        print("My name is " + self.name + " and I am " + str(self.age) + ".")

class Police(Person):
    def arrest(self, to_arrest):
        print("Freeze!!, " + to_arrest)

class Student(Person):
    def study(self, to_study):
        print("Study hard!!, " + to_study)

a = Person("Ahn", 29)
a.say_h("L")

b = Person("K", 1)
b.say_h("E")

c = Person("P", 2)
c.say_h("LEE")

aa = Person("Ahn", 29)
aa.say_h("Kim")
aa.intro()

kkk = Person("Kim", 25)
ppp = Police("Park", 55)
ahn = Student("Ayi", 29)

kkk.intro()
ppp.intro()
ahn.intro()

ppp.arrest("You")
ahn.study("Ahn")

dd = Dog()
dd.berk()

cc = Cat()
cc.meow()