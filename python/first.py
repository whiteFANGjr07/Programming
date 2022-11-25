import random
print("welcome to the RPS game")
user = input("Enter Your Choice:- \nRock\nPaper\n
Scissors")
print("\nYour input is :- ",user)

choices = ["Rock" , "Paper" , "Scissors"]
computer=random.choices

print(computer)
if(user=="rock" and computer=="paper"):
    print("\nYou Win")
elif(user=="rock" and computer=="scissors"):
   print("\nYou Loose")
elif(user=="paper" and computer=="rock"):
    print("\nYou Win")
elif(user=="paper" and computer=="scissors"):
    print("\nYou Loose")       
elif(user=="scissors" and computer=="paper"):
    print("\nYou Win")
elif(user=="scissors" and computer=="rock"):
    print("\nYou Loose")
else:
    print("\nTie")    
