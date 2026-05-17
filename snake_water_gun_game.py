import random
print("Welcome to Snake 🐍 Water🌊 and Gun 🔫Game🎉🎉")
computer_points=0
user_points=0
for i in range(1,4):
    user=int(input("Enter the number where 1 for snake 2 for water and 3 for Gun:"))
    computer= random.randint(1, 3)
    print("The options that you selected is :",user)
    print("The option that computer selectedd is ",computer)
  
    if user==1 and computer==1:
        print("Draw")
    elif user==1 and computer==2:
        print("Won")
        user_points+=1
    elif user==1 and computer==3:
        computer_points+=1
    elif user==2 and computer==1:
        computer_points+=1
    elif user==2 and computer==2:
        print("DRAW")
    elif user==2 and computer==3:
        user_points+=1
    elif user==3 and computer==1:
        user_points+=1
    elif user==3 and computer==2:
        computer_points+=1
    elif user==3 and computer==3:
        print("DRAW💰")
    else:
        print("Not Valid option❌")
print("The user points are:",user_points)
print("The computer points are:",computer_points)
if user_points>computer_points:
    print("User Won👱👱👱")
elif computer_points>user_points:
    print("Computer Won🖥️👩‍💻")
else:
    print("Draw")
print("Thank you For playing🎉🎉🎉🎉")


        


