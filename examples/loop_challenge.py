# nums = range(1, 51)
#
# for num in nums:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# factorial

def factorial(integer):
    nums = range(integer)
    result = 1
    for num in nums:
        result *= num + 1
    return result


print(factorial(5))

