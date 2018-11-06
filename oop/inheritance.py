# inheritance

class animal:
    type = "mammal"


class dog(animal):
    breed = "labrador"


my_dog = dog()

dogbreed = my_dog.breed

dogtype = my_dog.type

print(dogbreed)

print(dogtype)


# Overriding Class Attributes

class bird(animal):
    type = "bird"


my_bird = bird()

typeofbird = my_dog.type

print(typeofbird)


# Multitple Inheritance


class eagle(bird, animal):
    species = "eagle"

my_eagle = eagle()

eagleType = my_eagle.type

print(eagleType)


# Initializing a constructor

class my_complex:
    def __init__(self, real_part, imaginary_part):
        self.r = real_part
        self.i = imaginary_part

complex_num = my_complex(2, 3)

print(complex_num.i)


# Overriding Comparison Operators

class book:
    def __init__(self, pages):
        self.pages = pages

    def __lt__(self, other):
        return self.pages < other

    def __gt__(self, other):
        return self.pages > other



book1 =  book(42)

book1.title = "My Book"

print(book1.title)


class dog:
    def talk(self):
        print("bark")

class cat:
    def talk(self):
        print("meow")

def speak(animal):
    animal.talk()


mydogg = dog()

mycat = cat()

speak(mycat)

