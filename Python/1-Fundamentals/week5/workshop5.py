import random


def guess_random_number(tries: int, start: int, stop: int):
    """
        Guess a random number
    """
    between = random.randint(start, stop)
    while tries != 0:
        print("Tries remaining:", tries)
        guess = input("Please enter a guess: ")
        if int(between) == int(guess):
            print("Success!!")
            return None

        if int(guess) < int(between):
            print("Guess higher!")
            tries -= 1
        elif int(guess) > int(between):
            print("Guess lower")
            tries -= 1
    print("Failed!")


def guess_random_num_linear(tries: int, start: int, stop: int):
    """
        Linear search to gets a number
        Brute Force Style
    """
    between = random.randint(start, stop)

    for num in range(start, stop):
        if num == between:
            print("Success! Your guess", num, "Equals our guess!", between)
            break
        if num != between:
            tries -= 1
            print("Try again! Tries left", tries)
            if tries == 0:
                print("No Tries Left!", between, "Was the number")
                break


def guess_random_num_binary(tries: int, start: int, stop: int):
    between = random.randint(start, stop)
    print("Your target number", between)

    while tries:
        mid = (start + stop) // 2
        # mid_value =
        # the_list = []

        if mid == between:
            print("Success!", mid, "equals", between)
            return mid
        if mid > between:
            stop = mid-1
            print("Guess Lower! Tries left", tries,
                  "Left and your guess was", mid)
        if mid < between:
            start = mid+1
            print("Guess Higher! Tries left", tries,
                  "Left and your guess was", mid)
        tries -= 1
    print("Failed didn't find number")


guess_random_num_binary(5, 1, 100)
