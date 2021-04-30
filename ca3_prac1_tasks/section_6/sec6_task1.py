print("*"*60)
print("Section 6 if-else statement")
print("*"*60)
print()

number = input("Enter a number: ")

if number.isnumeric():
    print()
    if int(number) % 2 == 0:
        print(number + " is even")
    else:
        print(number + " is odd")
else:
    print("You did not enter a number")
