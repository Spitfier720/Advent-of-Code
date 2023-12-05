import sys

sum = 0
cardID = 1
cards = {}

for line in sys.stdin.readlines():
    cards[cardID] = cards.setdefault(cardID, 0) + 1
    line = line.split(":")[1].strip()
    win, cur = line.split("|")
    win = list(map(int, win.split()))
    cur = list(map(int, cur.split()))
    score = 0

    for i in range(len(win)):
        if win[i] in cur:
            score += 1
            cards[cardID + score] = cards.setdefault(cardID + score, 0) + cards[cardID]
    
    sum += cards[cardID]
    cardID += 1

print(sum)