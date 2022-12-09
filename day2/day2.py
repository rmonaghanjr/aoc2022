WIN = 'Z'
DRAW = 'Y'
LOSS = 'X'

ROCK = 1
PAPER = 2
SCISSORS = 3

with open("./input.txt", "r") as f:
    plays = [n.split(" ") for n in f.read().split("\n")]

    score1 = 0
    score2 = 0
    for play in plays:
        opp = ord(play[0]) - 64
        you = ord(play[1]) - 87

        if you == ROCK:
            if opp == PAPER:
                score1 += you
            elif opp == ROCK:
                score1 += 3 + you
            else:
                score1 += 6 + you
        elif you == PAPER:
            if opp == PAPER:
                score1 += 3 + you
            elif opp == ROCK:
                score1 += 6 + you
            else:
                score1 += you
        elif you == SCISSORS:
            if opp == PAPER:
                score1 += 6 + you
            elif opp == ROCK:
                score1 += you
            else:
                score1 += 3 + you
        
        outcome = play[1]
        if outcome == LOSS:
            if opp == ROCK:
                score2 += 3
            elif opp == PAPER:
                score2 += 1
            elif opp == SCISSORS:
                score2 += 2
        elif outcome == WIN:
            if opp == ROCK:
                score2 += 2
            elif opp == PAPER:
                score2 += 3
            elif opp == SCISSORS:
                score2 += 1
        elif outcome == DRAW:
            score2 += opp

        score2 += (ord(outcome) - 88) * 3
    
    print(score1)
    print(score2)


        

