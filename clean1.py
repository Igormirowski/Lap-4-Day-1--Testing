
import requests
        # 1.
def do_maths(x, y):
    return x +y


        # 2. add to array function 
def add_fruit(fruit, salad):
    salad.append(fruit)
    return salad

        # 3. Num of sweets Error

class StuffError(Exception):
    pass

def how_many_sweets(sweets, people):
    if not people:
        raise StuffError("We need some people to share sweets with!")
    return len(sweets) / len(people)


        # 4. greeting

def greeting(name):
    print (f"Hello, {name}!")

        # 5. cats
cats = []
def find_cat_by_id(cat_id):
    return next(cat for cat in cats if cat['id'] == cat_id)


            # API 
def fetch_stuff():
    req = requests.get("https://api.github.com/users/getfutureproof")
    data = req.json()
    print(f"Email is {data['email']}")

fetch_stuff()


if __name__ == "__main__":

    greeting('Beth')
