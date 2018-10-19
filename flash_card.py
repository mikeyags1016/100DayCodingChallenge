import random

flash_cards = {}


def add_flash_card(front, back):
    flash_cards.update({front: back})


def trivia_mode(cards):
    selected_keys = []
    i = 0

    while i < len(cards):
        current_selection = random.choice(tuple(cards.keys()))
        if current_selection not in selected_keys:
            guess = input(current_selection + ": ")

            if guess == cards[current_selection]:
                selected_keys.append(current_selection)
                i += 1
            else:
                print("Wrong, answer: " + cards[current_selection])

