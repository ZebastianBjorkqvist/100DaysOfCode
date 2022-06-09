from replit import clear
from art import logo

bidders = {}


def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


print(logo)
print("Welcome to the secret auction program")

continue_adding = True
while continue_adding:

    name = input("What is your name?")
    bid = int(input("What is yor bid?"))

    bidders[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'")
    if more_bidders == "no":
        continue_adding = False
    clear()

find_highest_bidder(bidders)
