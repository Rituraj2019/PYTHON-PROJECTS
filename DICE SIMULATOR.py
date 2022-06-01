import random  #inbuilt module
print("welcome to the dice simulator, enjoy")
roll=input(" Do you want to roll the dice? (y/n): ") #asking the user if he/she wish to roll the dice or not
if roll =='y':
    result=random.randint(1,6)   #if yes, using rand.int method of random module for number btwn 1-6 of a dice
    print(result)

elif roll=='n':
    print()
    print("Thank you!")
    exit   #if no, exit

else:               #invalid input from user
    print()
    print("INVALID INPUT; Please give valid input, either y or n")