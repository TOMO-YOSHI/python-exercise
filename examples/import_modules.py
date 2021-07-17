# import random
#
# print(random.randint(1, 10))

# function import
# from random import randint
#
# print(randint(10, 12))

# universal import
# from random import *
#
# print(random())

# Scope
example = "hello world"


def loc_ex():
    # global example
    example = "This is a string."
    return example


print(loc_ex())

print(example)

