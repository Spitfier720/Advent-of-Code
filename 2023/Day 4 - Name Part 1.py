import sys

sum = 0

for line in sys.stdin.readlines():
    line = line.split(":")[1].strip()
    win, cur = line.split("|")
    win = list(map(int, win.split()))
    cur = list(map(int, cur.split()))
    score = 0

    for i in range(len(win)):
        if win[i] in cur:
            if(score == 0):
                score = 1
            
            else:
                score *= 2
    
    sum += score

print(sum)