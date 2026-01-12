from itertools import product, combinations

suit = list(range(4))
rank = list(range(13))

cards = product(suit, rank)

count = 0
total = 0

for c in combinations(cards, 6):
    total += 1
    
    if total % 100000 == 0:
        print(total, "/", 20358520)

    good = True
    suits = {}
    ranks = set()

    for card in c:
        if card[1] in ranks:
            good = False
            break
        else:
            ranks.add(card[1])

        if card[0] in suits:
            suits[card[0]] += 1
        else:
            suits[card[0]] = 1

    if good:
        for s in suits:
            if suits[s] == 1:
                good = False
                break

    if good:
        if count % 10000 == 0:
            print(list(suits.values()))
            print(c)
        count += 1

print(count)
