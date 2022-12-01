# Day 1 Solution
with open("./input.txt", "r") as f:
    contents = f.read().split("\n\n")

    max_c = 0
    h = []
    for bag in contents:
        c = sum([int(n) for n in bag.split("\n")])
        h.append(c)
        if c > max_c:
            max_c = c
    # part 1        
    print(max_c)

    # part 2
    print(sum(sorted(h)[-3:]))
        
        
