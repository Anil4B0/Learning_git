print("Welcome to my Game")

playing_game = input("Do you want to play (yes or no)? ")

if playing_game != "yes":
    quit()

print("Let's play :)")

score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does CP stands for? ")
if answer.lower() == "central processing":
    print("correct!")
    score += 1
else:
    print("Incorrect")
answer = input("What does U stands for? ")
if answer.lower() == "unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

print("your score is" + str(score))
print("your percentage is " + str(score/3*100))