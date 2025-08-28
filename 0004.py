import random

print("welcome to (rock , paper , scissors) game . ")
input("Enter press to continue ....")
A=input("Enter your choice (Rock , Paper , Scissors) : ")
list=["Rock" , "Paper" , "Scissors"]
CC=random.choice(list)

if A.capitalize() == "Rock" :
  print()
  print("Your choice is ")
  print()
  print("""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")


elif A.capitalize() == "Paper" :
  print()
  print("Your choice is ")
  print()
  print(""" _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
  
elif A.capitalize() == "Scissors" :
  print()
  print("Your choice is ")
  print()
  print("""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")

else :
  print ("Invalid choice .")

print()


if CC.capitalize() == "Rock" :
  print ("Computer choice is :")
  print()
  print("""   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif CC.capitalize() == "Paper" :
  print ("Computer choice is :")
  print()
  print("""    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""")
elif CC.capitalize() == "Scissors" :
  print ("Computer choice is :")
  print()
  print("""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")