print("Welcome to this Quiz!")

is_playing = input ("Hi there! Do you want to play? ")
if is_playing.lower() != "yes":
  quit()

print("Great! Let's play then...")
score = 0

quiz1= input("What does html stand for? ")
if quiz1.lower() == "hyper text markup language":
  print("Correct!")
  score +=1
else:
  print("Ops wrong!")

quiz2= input("What does css stand for? ")
if quiz2.lower() == "cascading style sheet":
  score +=1
  print("Correct!")
else:
  print("Ops wrong!")
 
quiz3= input("What does Js stand for? ")
if quiz3.lower() == "javascript":
  score +=1
  print("Correct!")
else:
  print("Ops wrong!")

print(f"Thanks for playing this quiz. Your score is {score} & the score percentage is {(score /3)*100} %")