from cat_class import Cat
from cat_class import GoodCat
from cat_class import BadCat
from cat_class import VeryBadCat
from cat_class import cat_cage

print("All cats are in a cage.")

cat1: Cat = GoodCat()
cat2: Cat = BadCat()
cat3: Cat = VeryBadCat()

@cat_cage
def run_in_cage():
        
    cat1.meow()
    cat2.meow()
    cat3.meow()

run_in_cage()