import sys

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if(arr[j][0] < arr[j + 1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            elif(arr[j][0] == arr[j + 1][0]):
                for x in range(5):
                    if(strengths.index(arr[j][1][x]) < strengths.index(arr[j + 1][1][x])):
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        break

                    elif(strengths.index(arr[j][1][x]) != strengths.index(arr[j + 1][1][x])):
                        break
    
    return arr

strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
ranks = []

for line in sys.stdin.readlines():
    cards, bet = line.split()
    freqs = {}

    for c in cards:
        freqs[c] = freqs.setdefault(c, 0) + 1
    
    maxFreq = max(freqs.values())

    if(maxFreq == 5):
        ranks.append((1, cards, bet))
    elif(maxFreq == 4):
        ranks.append((2, cards, bet))
    elif(maxFreq == 3):
        if(2 in freqs.values()):
            ranks.append((3, cards, bet))
        else:
            ranks.append((4, cards, bet))
    elif(maxFreq == 2):
        if(list(freqs.values()).count(2) == 2):
            ranks.append((5, cards, bet))
        else:
            ranks.append((6, cards, bet))
    else:
        ranks.append((7, cards, bet))
    
ranks = bubbleSort(ranks)
totalWinnings = 0

for r in range(len(ranks)):
    totalWinnings += int(ranks[r][2]) * (r + 1)

print(totalWinnings)
