s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
s3 = input("Enter string 3: ")

print("Length of string 1 {} is {}".format(s1, len(s1)))
print("Length of string 2 {} is {}".format(s2, len(s2)))
print("Length of string 3 {} is {}".format(s3, len(s3)))

print("String 1 in all caps " + s1.upper())

substring = "a"
if substring in s2:
    print(s2.find(substring))
else:
    print("The letter {} is not found in {}".format(substring, s2))

print("The first 2 characters of {} is {}".format(s3, s3[0:2]))
