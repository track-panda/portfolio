import random

random_number = random.randrange(0,3)

RPS = input("rock, paper, scissors!").strip()
if(random_number == 0 and RPS == "paper"):
    print("Dang it! You win!")
if(random_number == 0 and RPS == "scissors"):
    print("Yay! I win!")
if (random_number == 0 and RPS == "rock"):
    print("Aww man, we tied! Let's go again!")

if(random_number == 1 and RPS == "paper"):
    print("Aww man, we tied! Let's go again!")
if(random_number == 1 and RPS == "scissors"):
    print("Dang it! You win!")
if(random_number == 1 and RPS == "rock"):
    print("Yay! I win!")

if(random_number == 2 and RPS == "paper"):
    print("Yay! I win!")
if(random_number == 2 and RPS == "scissors"):
    print("Aww man, we tied! Let's go again!")
if(random_number == 2 and RPS == "rock"):
    print("Dang it! You win!") 