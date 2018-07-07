import random

counter =0
guess = random.randint(1,10)

user_input = int(input("Guess the value: "))
counter = counter + 1  # can also be written as counter +=1

while(counter != 3):


    if(guess == user_input):
        print("Guess the value correctly after ", counter, " tries")
        break

    else:
        print("Wrong guess. you have tried", counter, "time(s). After 3 chances the game will end")
        user_input = int(input("Try again:  "))
        counter = counter + 1  # can also be written as counter +=1

    if(counter == 3):
        print("The value was: ", guess,  ". You are out of chances. The program is quitting!! ")