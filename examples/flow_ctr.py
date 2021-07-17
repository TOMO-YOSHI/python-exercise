# print(9 == "9")
#
# print("hello" == "Hello")
#
# print(4.0 == 4 or 1 < 0)
#
# print(4.0 == 4 and 1 < 0)

# veg = input("Enter the name of a vegetable.")
#
# if veg == "corn":
#     print("The veg is corn")
# else:
#     print("The veg is NOT corn")

# gpa = float(input("What was the applicant's grade point average?"))
#
# inst_app = input("Is the student going to be educated at an approved institution?")
#
# if gpa >= 3.7:
#     if inst_app == "yes":
#         print("The applicant qualifies for a low APR student loan.")
#     else:
#         print("The applicant does not qualify since they have not been accepted into an approved institution.")
# else:
#     print("The applicant did not have high enough grades to qualify")

score = int(input("What is your score?"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
