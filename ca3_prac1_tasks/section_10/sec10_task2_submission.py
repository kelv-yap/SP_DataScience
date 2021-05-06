import random


def oddandeven(numbers_list):
    odd = []
    even = []

    for number in numbers_list:
        if number % 2 == 0:
            odd.append(number)
        else:
            even.append(number)
    return odd, even


original_list = [random.randint(1, 1000) for x in range(100)]
print("Original List: {}".format(original_list), "\n")

odd_numbers, even_numbers = oddandeven(original_list)
print("Odd: {}".format(odd_numbers), "\n")
print("Even: {}".format(even_numbers))
