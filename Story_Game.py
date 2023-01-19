#level1

level1_done = False

while level1_done == True:
    print("What do you want? Y/N")
choice = input()
if    choice == "WALK":
    print("You walk forward the street and storm start")
    print("Jump to car? (Y/N)")
    sub_choice = input()
    if sub_choice == "Y":
        print("In car very warm and radio station on RockFM")
        level1_done = False
    else:
        print("Hey, its very sad, your car is empty...")
elif choice == "Drink":
    print("at the floor you see coca-colla")
elif choice == "CALL":
    print("Somebody changed radio station")
else:
    print("Maybe its a GoustWALK")

#level2
print("level 2")
level2_done = False
while level2_done == False:
    print("Nobody respond and you feel the storm stronger")
    choice = input("Call 911")
    if choice == "Y":
        print("The gelicopter came for save your life, they have hot chocolate!")
        print("level_next")
        level2_done = True
    else:
        print("Nobody respond")
        sub_choice2 = input("")
        if sub_choice2 == "EXIT":
            print("It was just a dream")
            level2_done = True
        elif sub_choice2 == "Finally not hungry":
            print("when our food finished we decide to get a nap")
            level2_done = True
