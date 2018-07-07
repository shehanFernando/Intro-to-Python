import random #to use randInt function

x = random.randint(0, 10)  # get a random value between 0-10
i = int(input("Guess the value: "))  # gets the user input

while (i != x and i != -1):  # keep on asking vaue till the answer is correct  or i = -1 to quit
    i = int(input("Guess is wrong! Either enter -1 to quit or -2 for a hint. Try again: "))

    if (i + 2 == x or i - 2 == x):  # if the gussed value is eithe +/- 2 tell the user that "Almost there"
        print("Almost there,try again: ")
        i = int(input("Almost there,try again: "))

    if i == -2:  # HInts
        if (x % 2 == 0):
            i = int(input("Number is an even number, try again: "))
        else:
            i = int(input("Number is an odd number, try again: "))

    if (i == -1):  # if user puts -1 then the program quits
        print("The Program is quitting! The value was: ", x)

if (i == x):  # prints the value if correct
    print("Yes, ", x, " is the correct answer!")
