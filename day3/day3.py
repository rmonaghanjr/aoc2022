with open("./input.txt", "r") as f:
    rucksacks = f.read().split("\n")

    sum_priorities = 0
    sum_groups = 0

    for sack in rucksacks:
        first_compartment = sack[0:len(sack)//2]
        second_compartment = sack[len(sack)//2:]

        shared = set(second_compartment).intersection(set(first_compartment))

        for item in shared:
            ascii = ord(item)

            if ascii >= 97:
                sum_priorities += ascii - 96
            else:
                sum_priorities += ascii - 38

    for i in range(2, len(rucksacks), 3):
        sack1 = set(rucksacks[i - 2])
        sack2 = set(rucksacks[i - 1])
        sack3 = set(rucksacks[i])
        
        shared = sack1.intersection(sack2)
        shared = shared.intersection(sack3)

        for item in shared:
            ascii = ord(item)

            if ascii >= 97:
                sum_groups += ascii - 96
            else:
                sum_groups += ascii - 38
    
    print(sum_priorities)
    print(sum_groups)