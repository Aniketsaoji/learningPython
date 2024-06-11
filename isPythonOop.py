# Objects delete after runtime
# Access Modifiiers include public, protected and private.
# public: x.y
# public access similar to java: accessible outside the class
# private. accessible within the class alone
# protected. Can only be used outside of the class if its from a subclass
# protected: x._y
# private: x.__y


class Person:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("RIP g")

    def sayHello(self):
        print("My name is: " + self.name)
aniket = Person("aniket")
sahil = Person("sahil")
print(aniket.name)
print(sahil.name)
aniket.sayHello()
