name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("you are old enough to vote")
    print("please put on X in block")
else:
    print("please come back in {0} years" .format(18-age))

ages =int(input("please enter your age : "))

if ages >=16 and ages <= 65:
    print("age bitween 16 and 65")
elif ages < 16:
    print("age is greater then 16 ")
elif ages > 65:
    print("age is less then 65")