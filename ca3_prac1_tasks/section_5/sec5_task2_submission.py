input_strings = input("Enter 3 random strings, separated by commas: ")

str_list = input_strings.split(sep=",")
s1 = str_list[0]
s2 = str_list[1]
s3 = str_list[2]

print("s1 is {}".format(s1))
print("Length of {} is {}".format(s1, len(s1)))
print("2nd and 3rd characters of {} is {}".format(s1, s1[1:3]))
print()

print("s2 is {}".format(s2))
print("Length of {} is {}".format(s2, len(s2)))
print("5th and 7th characters of {} is {}".format(s2, s2[4:7]))
print()

print("s3 is {}".format(s3))
print("Length of {} is {}".format(s3, len(s3)))
print("Last two characters of {} is {}".format(s3, s3[-2:]))
