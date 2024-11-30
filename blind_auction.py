from random import randint


names = ['Anna', 'Maria', 'Sofia']
bids = {name:randint(0, 301) for name in names}

print(bids)

winner = max(bids, key=bids.get)

print(f"Winner of auction is: {winner} with {bids[winner]}")
