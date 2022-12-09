with open("./input.txt", "r") as f:
    contents = f.read().split("\n\n")

    container_stacks_count = len(contents[0].split("\n")[len(contents[0].split("\n")) - 2].split(" "))
    containers = [[] for n in range(0, container_stacks_count)]
    containers_copy = []
    container_stack = []
    for line in contents[0].split("\n"):
        if not line.strip().startswith("["): # line is NOT a container line
            break

        c_num = 0
        for j in range(0, len(line), 4):
            container_name = line[j:j+3][1]

            if container_name != " ":
                containers[c_num] = [container_name] + containers[c_num]
            
            c_num += 1

    for stack in containers:
        temp = []
        for container in stack:
            temp.append(container)
        containers_copy.append(temp)
    
    instructions = contents[1].split("\n")

    for instruction in instructions:
        tokenized = instruction.split(" ")

        count = int(tokenized[1])
        from_n = int(tokenized[3]) - 1
        to_n = int(tokenized[5]) - 1

        containers[to_n] += reversed(containers[from_n][len(containers[from_n]) - count:])
        containers[from_n] = containers[from_n][:len(containers[from_n]) - count]

        containers_copy[to_n] += containers_copy[from_n][len(containers_copy[from_n]) - count:]
        containers_copy[from_n] = containers_copy[from_n][:len(containers_copy[from_n]) - count]

    msg = ""
    for c in containers:
        msg += c[len(c) - 1]

    msg2 = ""
    for c in containers_copy:
        msg2 += c[len(c) - 1]

    print(msg)
    print(msg2)
