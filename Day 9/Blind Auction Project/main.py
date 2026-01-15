# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def bid_winner():
    winner = max(auction_bids, key=auction_bids.get)
    print(f"Congratulations to the winner of our auction, {winner}, who made a bid of {auction_bids[winner]}!")
    # print(key_with_max_value)

    # highest_bidder = 0
    # bid_value = ""
    # for auction_bids[name] in auction_bids:
    #     if bid > highest_bidder:
    #         highest_bidder = bid
    #         print(bid)

more_bidders = True
print("Welcome to Kuboni\'s Auction House\n")
auction_bids = {}

while more_bidders:
    name = input("Please provide your first name?\n")
    bid = int(input("Please type in your bid? \nR "))
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    auction_bids[name] = bid
    if continue_auction == "yes":
         print("\n" * 2)
    elif continue_auction == "no":
        more_bidders = False
        bid_winner()
    else:
        print(f"Error, your input is invalid. Please try again:")
        continue_auction = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
        if continue_auction == "no":
            more_bidders = False
            bid_winner()
