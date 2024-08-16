class Cat:
    
    def meow(self):
        
        print("meow")

class GoodCat(Cat):

    def meow(self):
        print("purr purr meow")
    
class BadCat(Cat):

    def meow(self):
        print("hiss")

class VeryBadCat(Cat):

    def meow(self):
        raise Exception("Very bad cats need cages")

def cat_cage(f):
    def catch(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as error:
            print(f"Cat was bad: {error}, no harm was done due to Cage")
    return catch