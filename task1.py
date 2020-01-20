SYMBOL = "*"
SPACE = " "
ROWS = 7
SPACES_Q = ROWS - 1
STARS_Q = 1

for i in range(ROWS):
    print((SPACE * SPACES_Q) + (SYMBOL*STARS_Q))
    STARS_Q += 2
    SPACES_Q -= 1