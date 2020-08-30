
import random
user = 0 
print('''
Welcome to HandCricket Game . 
Play this game by selecting Numbers From 1 to 6
''')
score = 0
while user < 7:
  user = int(input("Enter your predicted Runs = > "))
  com = random.randint(0,6)
  # print(com)
  if user != com:
    score+=user
  else:
    print(f" You Gone For {score} Runs")
    break
  print(f"Your score is {score} Runs")
else:
  print("Your score is  out of Bound Runs")
