with open("./input.txt", "r") as f:
    contents = f.read()

    marker_start = -1
    for i in range(0, len(contents)):
        if len(set(contents[i:i+4])) == len(contents[i:i+4]):
            marker_start = i + 4
            break

    message_start = -1
    for i in range(0, len(contents)):
        if len(set(contents[i:i+14])) == len(contents[i:i+14]):
            message_start = i + 14
            break
    
    print(marker_start)
    print(message_start)