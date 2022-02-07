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

highest_bidder = {'bid': '0'}
for bidder in bidders:
  if (int(bidder["bid"]) > int(highest_bidder["bid"])):
    highest_bidder = bidder

print(f"The winning bidder is {highest_bidder['name']} with $ {highest_bidder['bid']}.")