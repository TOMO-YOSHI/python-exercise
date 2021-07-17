# string = "test"
#
#
# def function_name(param=1, pa=1):
#     return param + pa + 2
#
#
# ans = function_name(2, 2)
#
# print(ans)
#
#
# def hello_world_printer():
#     print("hello world")
#
#
# hello_world_printer()
#

# def name_printer(param):
#     print(param)
#
#
# name = input("enter your name.")
#
# name_printer(name)
#

# def calc(l, w, h):
#     return l * w * h
#
#
# length = int(input('enter length'))
# width = int(input('enter width'))
# height = int(input('enter height'))
#
# print("The volume of the rectangular prism is " + str(calc(length, width, height)) + " cubic feet.")

def fahrenheit(cel):
    return (18 * cel + 320) / 10


userInput = int(input("enter celsius temp(integer)"))


print("The Fahrenheit equivalent of " + str(userInput) + " degrees Celsius is " + str(fahrenheit(int(userInput))))
