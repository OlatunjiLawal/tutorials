from cat_class import Cat

class GoodCat(Cat):

    def meow(self):
        print("purr purr meow")
    
class BadCat(Cat):

    def meow(self):
        print("hiss")

class VeryBadCat(Cat):

    def meow(self):
        raise Exception("Nope. scratch scratch")

print("Good cats go...")
cat: Cat = GoodCat()
cat.meow()

print("Bad cats go...")
cat: Cat = BadCat()
cat.meow()

print('very bad cats need cages')
cat: Cat = VeryBadCat()
cat.meow()
