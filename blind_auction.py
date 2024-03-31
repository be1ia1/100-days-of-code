from random import randint


names = ['Anna', 'Maria', 'Sofia']
bids = {}
for name in names:
    bids[name] = randint(0,301)

print(bids)

name = 'Anna'
max_bid = bids["Anna"]

for k,v in bids.items():
    if v > max_bid:
        max_bid = v
        name = k


print(f"Winner of auction is: {name} with {max_bid}")
    


