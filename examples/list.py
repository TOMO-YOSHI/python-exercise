# example_list = [10, 3.14, "tree", False, [1, 2, 3]]

# print(example_list[1:3])
#
# print(list("Tomohiro"))
#
# checked_list = [1, 2, 3, 4]
# print(1 in checked_list)
# print(8 in checked_list)
# print(8 not in checked_list)

# list_2 = [[0, 2], [4, 6], [8, 10], [12, 14]]
#
# print(list_2[0])
# print(list_2[-1][-1])
#
# list_3 = ["chair", "table", "desk", "lamp", "bed"]
#
# print(list_3[len(list_3) * -1])
#
# print("Most people own at least {} {}s.".format(list_2[0][1], list_3[len(list_3) * -1]))
#
# list_4 = [0.98, 8.76, 6.54, 4.32]
#
# print(list_4[1:])
#
# print(list_4[1:-1])
#
# print(list_4[:2])

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

del arctic_animals[-2]

print(arctic_animals)

arctic_animals.remove("elephant")

print(arctic_animals)

arctic_animals.append("arctic fox")

print(arctic_animals)

arctic_animals.insert(2, "snowy owl")

print(arctic_animals)

arctic_animals.sort()

print(arctic_animals)

print(arctic_animals.index("reindeer"))

last_item = arctic_animals.pop(0)

print(last_item)
