from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print("Welcome to Magda's silent auction")
print(logo)
bid_continue = True

bidders = []
def add_new_bidder(bid_name, bid_value):
    new_bidder = {}
    new_bidder["name"] = bid_name
    new_bidder["bid"] = bid_value
    bidders.append(new_bidder)


while bid_continue:
  name = input("What's your name? ")
  bid = input("What's your bid? $")
  add_new_bidder(name, bid)

  other_bid = input("Anyone else want's to bid? Type yes or no ").lower()
  if other_bid == "yes":
    clear()
  else:
    bid_continue = False

bid_values_list = []

for bidder in bidders:
  bid_values_list.append(int(bidder["bid"]))

max_value= max(bid_values_list)

max_index = bid_values_list.index(max_value)
winner_bid = bidders[max_index]
print(f"The winning bidder is {winner_bid['name']} with $ {winner_bid['bid']}.")