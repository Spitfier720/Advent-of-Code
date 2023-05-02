#Finding whether a character on the opposite side of a circular string is the same as a given character.

captcha = input()
length = len(captcha)
total = 0

for x in range(length // 2):
    if(captcha[x] == captcha[(x + (length // 2)) % length]):
        total += int(captcha[x]) * 2

print(total)