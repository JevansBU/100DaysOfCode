print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Your Boyfriend's Treasure Hunt :)")
print("Your mission is to find the Great Bean Treasure.")
pts = 0

choice1 = input("You have come across two paths, one leads to a dark 'woods' and the other "
                " a small 'pond', which do you take my bean x: ").lower()
if choice1 == "pond":
    pts += 5
    print(f"Total Points = {pts}")
    print("Well done poopie, best to stay away from dark places")
    choice2 = input("You met a GREEN LIGHT! by the pond and he offers you three items, 'ladder', 'binoculars' and a 'wand'"
                    " ,which do you take Kochanie?: ").lower()

    if choice2 == "ladder":
        pts+= 5
        print(f"Total Points = {pts}")
        print("Yes you smart fartle, the ladder will come in handy")
        choice3 = input("Your about to approach the castle but then CHICO-SHINSKI JUMPS OUT ON YOU!!"
                        " ,what do you do? 'run' or 'jestes'?: ").lower()

        if choice3 == "jestes":
                pts += 5
                print(f"Total Points = {pts}")
                print("Chico shinski is now a happy dean and gave you some licks, he accompanies you on your journey to find the bean treasure!!")
                choice4 = input("You have made it to the entrance of the castle!! You're met by two guards that ask you a riddle. The riddle is"
                                " 'I go on red, but stop for green. What am I doing?'. Are you, eating a 'watermelon', at traffic 'lights' or starting a 'race'?: ").lower()

                if choice4 == "watermelon":
                    pts += 5
                    print(f"Total Points = {pts}")
                    print("Well Done Turtoid!! You successfully entered the Castle!!!")
                    choice5 = input("once in the Castle you see a ledge but you cant get up to it, what item that you collected earlier could you use to get up?:")

                    if choice5 == "ladder":
                        pts += 5
                        print(f"Total Points = {pts}")
                        print("Oooooo, my smart Bean, you are getting close to the treasure!!!!")
                        choice6 = input("You reached the Chamber room and you see the TREASURE!! however, the Treasure is guarded by a really angry MAMUSIA!!!!"
                                        " she's about to start sprinting towards you, how do you defend yourself? 'ladder', 'tatusia', 'chico', 'gun'?: ").lower()

                        if choice6 == "chico":
                            pts += 5
                            print(f"Total Points = {pts}")
                            print("Mamsuia stopped sprinting because she saw Chico the Dean, shes now distracted whilst you sneak of the claim the Bean Treasure!")
                            print()
                            print()
                            print("Congrats Kochanie, you found the bean treasure and made everyone happy, well done!!! BEANNNNN")

                        elif choice6 == "tatusia":
                            pts += 0
                            print(f"Total Points = {pts}")
                            print("Tatusia got slapped up and is now singing Miłość w Zakopanem whilst knocked out!!! ")

                        elif choice6 == "gun":
                            pts += 0
                            print(f"Total Points = {pts}")
                            print("Mamusia is bulletproof!, the bullets deflect and hit you in d face!")

                        else:
                            pts += 0
                            print(f"Total Points = {pts}")
                            print("Mamusia just yanked the ladder out of your hand and repeatedly beated you until death")

                    else:
                        pts += 0
                        print(f"Total Points = {pts}")
                        print("It was the ladder Kochanie from the Green Light Man, you was so close >:(")

                elif choice4 == "ligths":
                    pts += 0
                    print(f"Total Points = {pts}")
                    print("Incorrect answer, the guards chopped you up and chico ran away to hide :(")

                else:
                    pts += 0
                    print(f"Total Points = {pts}")
                    print("It was not a race :( The guards stuck there spears up your bum bum")
        else:
                pts += 0
                print("Chico is upset that you ran from him, Tatusia has skinned you alive for upseting the Dean")
                print(f"Total Points = {pts}")

    elif choice2 == "binoculars":
        pts += 0
        print("The binoculars had glue on them and are now stuck to your eyes forever :(")
        print(f"Total Points = {pts}")

    else:
        pts += 0
        print("The Green Light pulled down your pants and stuck his wand your your pupa :(")

else:
    pts += 0
    print("Oh my bean, you lasted 5 minutes in the woods before you tripped on a stick and slept for too long")
    print(f"Total Points = {pts}")




