season = input("What season is it?").strip()
if season == "winter":
 print("That explains why it is so cold!")
elif season == "spring":
 print("That explains why I'm sneezing")
elif season == "summer":
 print("That explains why it's so hot!")
elif season == "fall":
 print("That explains why the leaves are so colorful")
else:
 print("yo ", season, " is not a season")

color = input("What is your favorite color?").strip()
if color == "red":
 print("Eww, why do you like",color,".")
 input()
elif color != "red":
 print("I love the color",color,"too.")

name = input("What is your name?").strip()
if name == "emmy":
 print("Hello emmy!")
elif name != "emmy":
 print("What a cool name",name,".")

 animal = input("What is your favorite animal?").strip()
if animal == "panda":
 print("I love pandas too!")
elif animal != "panda":
 print("I don't like",animal,".")

 age = int(input("How old are you?").strip())
if age <= 10:
   print("You are not old enough to play competitive sports.")
if age > 10:
 print("You are old enough to play competitive sports!")

age_2 = int(input("How many years are you?").strip())
if age_2 < 16:
 print("You are not old enough to drive!")
if age_2 >= 16:
 print("Congratulations! You are old enough to drive!")

food = input("What is your favorite type of food?").strip()
if food == "pizza":
 print("I also love pizza!")
else:
 print("I don't really like",food,".")

fruit = input("What is the best fruit?").strip()
if fruit == "strawberries":
 print("No! Strawberries are the worst!")
if fruit == "watermelon":
 print("I like watermelon, but it is not the best.")
else:
 print("I agree!",fruit," are the best!")

number = int(input("Give me a number between 0 and 100.").strip())
if number > 0:
 if number < 100:
   print("You owe me",number,"bucks!")

week = input("Name a day of the week.").strip()
if week == "sunday":
 print("Good job that's correct!")
if week == "monday":
 print("Good job that's correct!")
if week == "tuesday":
 print("Good job that's correct!")
if week == "wednesday":
 print("Good job that's correct!")
if week == "thursday":
 print("Good job that's correct!")
if week == "friday":
 print("Good job that's correct!")
if week == "saturday":
 print("Good job that's correct!")
else:
 print("That isn't a day of the week!")

book = input("What is your favorite book?").strip()
if book == "Maze Runner":
 print("I love that book!")
elif book == "Hunger Games":
 print("I love that book!")
else:
 print("I have never read that book before. Is it good?")
input()

cone = input("Hey! Did you steal that traffic cone?").strip()
if cone == "yes":
 print("You thief!")
elif cone == "no":
 print("Ok good, I was just making sure.")

fav_character = input("What is your favorite character?").strip()
if fav_character == "Edna Mode":
 print("I LOVE EDNA MODE!")
if fav_character != "Edna Mode":
 print("IT NEEDS TO BE EDNA MODE!")

subject = input("What was your favorite subject in school?").strip()
if subject == "history":
 print("I loved history too! What was the event you found the most interesting?")
input()
if subject != "history":
 print("Oh really?",subject,"was my least favorite.")

music = input("What is your favorite decade of music?").strip()
if music == "seventies":
 print("I loved the seventies!")
if music == "eighties":
 print("I loved the eighties!")
if music == "nineties":
 print("I loved the nineties!")
if music == "two thousands":
 print("I loved the two thousands!")
else:
 print("Are you messing with me? Are you sure that is even a decade of music?")
input()

class_grade = float(input("What did you score on the test?").strip())
class_grade = round(class_grade)
if class_grade >= 90:
 print("Congrats you got an A!")
if class_grade >= 80 and class_grade <= 89:
   print("Congrats you got a B!")
if class_grade >= 70 and class_grade <=79:
   print("Congrats you got a C!")
else:
 print("Oh no! You failed the test!")

water_bottle = input("What is the brand of your metal water bottle?").strip()
if water_bottle == "stanley":
 print("How basic!")
elif water_bottle == "hydroflask":
 print("Those went out of style years ago!")
else:
 print("I have never heard of that one! Is it popular?")
input()

fav_teacher = input("Who is your favorite teacher?").strip()
if fav_teacher == "Mr. Stone":
 print("I hate Mr. Stone!")
else:
 print("I love",fav_teacher,"!")

puzzles = input("Do you like puzzles?").strip()
if puzzles == "yes":
 print("I also love puzzles!")
if puzzles == "no":
 print("How could you not love puzzles?!")
input()

speed_limit = int(input("What is the speed limit on this road?").strip())
if speed_limit == 60:
 print("That is pretty fast for a backroad!")
elif speed_limit > 60:
 print("That is extremely fast!")
elif speed_limit < 60:
 print("That seems kinda slow, if I am going to be honest.")

discus_distance = int(input("How far can you throw the discus,in feet?").strip())
if discus_distance >= 100:
 print("Wow that is really far!")
elif discus_distance < 100:
 print("That's ok! You will definitely improve during the school year!")

