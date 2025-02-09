
while(True):
    prompt = "Give me a number between 1 and 1,000: "
    range = int(input(prompt).strip())

    if (range) % 3 == 0 and (range) % 5 == 0:
        print("FizzBuzz")

    elif (range) % 3 == 0:
        print("Fizz")

    elif (range) % 5 == 0:
        print("Buzz")

    else: 
        print("That number is not divisble by 3 or 5! No FizzBuzz! Loser!")
        next
    
