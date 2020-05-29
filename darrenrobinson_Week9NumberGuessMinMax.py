import random

print('Hello! What is your name?')
player_name = input()

print("Hello, " + player_name + ". Guess a number between 1 AND 100 ")
answer = random.randint(0, 100)

#set number of guess as zero
attempts = 0

#set the number of maximum allowable attempts
attempts_max = 7

print("You will get", attempts_max, "tries to get it right.")

#set maximum variables     
max1 = 100
max2 = 100


#set minimum variables
min1 = -100
min2 = -100

def write_file(): #function to make a file called gamereport and add the player name and attempts
        f = open("gamereport.txt", "a")
        f.write("Player Name: " + player_name + "    Number of Attempts: " + str(attempts) + "\n")
        f.close()

while attempts < attempts_max:
    guess = int(input())
    if guess == answer:
        print("Wow! You got it," + player_name + "! The correct answer is", answer)
        print("You got the correct answer in", attempts + 1, "attempts")
        write_file()
       
    elif guess < answer:
        print("Strike " + str(attempts + 1) + ", " + player_name + ". Your guess was too low.")
        max1 = guess
        min1 = guess

        attempts = attempts + 1
          
    elif guess > answer:
        print("Strike " + str(attempts + 1) + ", " + player_name + ". Your guess was too high.")
        max2 = guess
        min2 = guess

        attempts = attempts + 1

if guess != answer:
    answer = str(answer)
    print("Sorry, " + player_name +  ". No more chances. The correct number was " + answer)


write_file()

