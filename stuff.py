
import requests
        # 1.
def do_maths(x, y):
    return x +y



        # 2. add to array function 
def add_fruit(fruit, salad):
    salad.append(fruit)
    return salad

# Extra check in terminal
salad = ["apple", "pear"]
fruit = "banana"

add_fruit(fruit, salad)
print (salad)


        # 3. Num of sweets Error

# define stuff error class
class StuffError(Exception):
    pass

def how_many_sweets(sweets, people):
    if not people:
        raise StuffError("We need some people to share sweets with!")
    return len(sweets) / len(people)

# We got 1.5 sweets per peopl/ if last list is empty we print message line 26
print(how_many_sweets(["sw1", "sw1", "sw3"], [1, 2])
)


        # 4. greeting

def greeting(name):
    print (f"Hello, {name}!")




        # 5. cats
cats = []
# cats = [{'id': 1, 'name': 'Garfield'}, {'id': 2, 'name': "Felix"}]
def find_cat_by_id(cat_id):
    return next(cat for cat in cats if cat['id'] == cat_id)

# # 2nd way of line 49
#     for cat in cats:
#         if cat['id'] == cat_id:
#             return cat
# # 3rd way of line 49 (comprehention list)
# [cat for cat in cats if cat['id'] == cat_id]


def fetch_stuff():
    req = requests.get("https://api.github.com/users/getfutureproof")
    data = request.json()
    print(f"Email is {data["email]"}")


if __name__ == "__main__":
    # how_many_sweets([1,2], [])

    greeting('Beth')
