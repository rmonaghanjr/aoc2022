with open("./input.txt", "r") as f:
    contents = f.read().split("\n")

    assignments = []

    for pair in contents:
        
        parsed_pair = pair.split(",")
        rebuilt_pair = []
        for elf in parsed_pair:
            _range = elf.split("-")
            rebuilt_pair.append((int(_range[0]), int(_range[1])))
        assignments.append(sorted(rebuilt_pair, key=lambda pair: pair[1] - pair[0])) # sort to have larger range on top
    
    fully_contained = 0
    partially_contained = 0

    for assignment in assignments:
        parent = assignment[1]
        child = assignment[0]

        if child[0] >= parent[0] and child[1] <= parent[1]:
            fully_contained += 1
        if parent[0] <= child[0] <= parent[1] or parent[0] <= child[1] <= parent[1]:
            partially_contained += 1

    print(fully_contained)
    print(partially_contained)
