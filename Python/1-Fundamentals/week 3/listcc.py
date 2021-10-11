import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    your_card = [0]
    card = input("Pick a card, or press Q to quit ")

    if card == "Q":
        break
    if not diamonds:
        print("No more cards")
    else:
        your_card = random.choice(diamonds)
        hand.append(your_card)
        print("Your card is", your_card)
        diamonds.remove(your_card)
        print(hand)
        print("Remaining Cards", diamonds)
