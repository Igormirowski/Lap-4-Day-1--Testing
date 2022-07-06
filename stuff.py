

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

if __name__ == "__main__":
    how_many_sweets([1,2], [])
