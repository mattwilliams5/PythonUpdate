import random

high_score = 0
total_score = 0


def dice_game():
    while True:
        print("1) Roll dice")
        print("2) Leave game")
        choice = (input("Please enter your choice: "))
        global total_score
        if choice == "1":
            roll_1 = random.randint(1, 6)
            print("First roll is", roll_1)
            roll_2 = random.randint(1, 6)
            print("Second roll is", roll_2)
            total_score = roll_1 + roll_2
            print("Your total score is", total_score)

        if high_score < total_score:
            print("You have a New High score of ", total_score)

        if choice == "2":
            print("Good day")
            break


dice_game()
