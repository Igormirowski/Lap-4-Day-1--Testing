


def do_maths(x, y):
    return x +y



# add to array function 
def add_fruit(fruit, salad):
    salad.append(fruit)
    return salad

# Extra check in terminal
salad = ["apple", "pear"]
fruit = "banana"

add_fruit(fruit, salad)
print (salad)


# Num of sweets Error

def how_many_sweets(sweets, people):
    if not people:
        raise Exception("We need some people to share sweets with!")
    return len(sweets) / len(people)
