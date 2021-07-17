# consoles = {"nintendo": "wii", "sony": "playstation"}
# print(consoles["sony"])
#
# mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4, False: 5}
# print(mixed[False])
#
# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# print(1 not in first)

# new_dic = {1: "test",
#            2: "test-2",
#            3: "test-3"}
#
# print(new_dic[3])
#
# print(4 in new_dic)
#
# print(5 not in new_dic)


# dic = {"Queen": "Bohemian Rhapsody",
#        "Bee Gees": "Stayin' Alive",
#        "U2": "One",
#        "Michael Jackson": "Billie Jean",
#        "The Beatles": "Hey Jude",
#        "Bob Dylan": "Like A Rolling Stone"}
#
# print(len(dic))
#
# for key in dic.keys():
#     print(key)
#
#
# print(dic.values())
#
# for key, value in dic.items():
#     print(key, value)
#
# print(dic.get("Promise of the Real", "Not found"))
# print(dic.get("Bob Dylan", "Not found"))

# ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
# print(ex_1)

# for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
#     print(key, value)

# fast_food_items = {"McDonald's": "Big Mac",
#                    "Burger King": "Whopper",
#                    "Chick-fil-A": "Original Chicken Sandwich"}
#
# print(fast_food_items["McDonald's"])
#
# fast_food_items.popitem()
#
# print(fast_food_items)

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)

print(internet_celebrities)

second_one = {"Hikakin": "YouTube"}

internet_celebrities.update(second_one)

print(internet_celebrities)

internet_celebrities.clear()

print(internet_celebrities)

print(second_one)
