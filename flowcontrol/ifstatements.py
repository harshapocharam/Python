name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age > 18:
    print("you are old enought to vote")
    print("please enter your in box")
else:
    print("Please come back in {0} years".format(18- age))


if age < 18:
    print("Please come back in {0} years". format(18- age))
elif age == 900:
    print("sorry, its not valid")
else:
    print("you are old enought to vote")
    print("Please put an x in the box")

