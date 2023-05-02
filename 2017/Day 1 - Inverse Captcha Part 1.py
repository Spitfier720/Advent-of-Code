#Finding whether a character on the right side of a circular string is the same as a given character.

captcha = input()
total = 0

for x in range(len(captcha)):
    if(captcha[x] == captcha[(x + 1) % len(captcha)]):
        total += int(captcha[x])

print(total)