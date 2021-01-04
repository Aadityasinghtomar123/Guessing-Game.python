import random

chance = 0
num = random. randint(1,9)
while chance < 5:
    guess=int(input("enter your guess"))
    if guess == num:
        print("Congratulation you won")
    elif guess<num:
        print("guess a number higher then ",num)
    elif guess>num:
        print("guess a number lower then ",num)
    chance+=1

if not chance < 5:
    print("You lose the number is ",num)    
                    
