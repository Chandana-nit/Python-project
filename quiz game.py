print("welcome to my computer quiz")

playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()

print("okay! lets play ")
score = 0

answer = input("what is python ?")
if answer.lower() == "python is a programming language":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what is oop ?")
if answer.lower() == "object oriented program":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what is VS code used for ?")
if answer.lower() == "for coding":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + "questions correct")
print("you got " + str((score / 3) * 100) +  "correct")

