name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("you are old enough to vote")
    print("please put on X in block")
else:
    print("please come back in {0} years" .format(18-age))

