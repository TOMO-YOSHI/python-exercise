# all_low = "this is a test"
#
# print(all_low.upper())
# print(all_low)
#
# all_up = "ALL UPPER"
# print(all_up.lower())
# print(all_up.isupper())
# print(all_up.islower())

# mixed_case = "A Song of Ice and Fire"
#
# print(mixed_case.isupper())
# print(mixed_case.islower())
# print(mixed_case.upper())
# print(mixed_case.lower())
# print(mixed_case.istitle())
#
# title_case = mixed_case.title()
#
# print(title_case)
# print(title_case.endswith("e"))
#
# words = mixed_case.split()
# print(words)
#
# print("".join(words).isalpha())

# print("hello world".ljust(15) + "four spaces later.")

# the_string = "North Dakota"
#
# print(the_string.ljust(17))
#
# center_plus = the_string.center(16, "+")
#
# print(center_plus)
#
# the_string.lstrip("North")
#
# print("***")
#
# print(the_string.lstrip("North"))
#
# print(center_plus)
#
# print(center_plus.strip("+"))
#
# print(the_string.replace("North", "South"))

# var = input("Please enter something!")
# empStr = ""
#
# for char in var:
#     empStr = char + empStr
#
# print(empStr)

var = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
# newStr = ""
# for char in var:
#     if char.isalnum() or char.isspace() or char == "-":
#         newStr += char
#     # elif char == "'":
#     #     newStr += " " + char + " "
#
#
# print(newStr.split())
# print(len(newStr.split()))

spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in var:
    if char.isalnum() or char.isspace() or char == "-":
        spaces_and_letters += char

words = spaces_and_letters.split()
number_of_words = len(words)

print(words)
print(number_of_words)

