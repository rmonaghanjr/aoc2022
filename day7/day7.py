MAX_SUM = 100000
MAX_SPACE = 70000000
NEEDED_SPACE = 30000000

# for part 2, writig this while i have it
# choose the smallest one that surpasses the diff of needed_space - (dir_size - needed_space)

class Node:
    def __init__(self, parent: "Node", name: str, directories: dict[str, "Node"], files: list[tuple]):
        self.parent = parent
        self.name = name
        self.directories = directories
        self.files = files

    def dir_size(self) -> int:
        r = sum([f[0] for f in self.files] + [self.directories[d].dir_size() for d in self.directories])
        return r

    def solve(self):
        count = 0
        for d in self.directories:
            s = self.directories[d].dir_size()
            count += s if s <= MAX_SUM else 0
            count += self.directories[d].solve()
        return count

def smallest_deletable(n: Node, unused: int) -> int:
    possible = []
    for dir in n.directories:
        r = smallest_deletable(n.directories[dir], unused)
        if r + unused >= NEEDED_SPACE:
            possible.append(r)
    possible.append(n.dir_size())

    return min(possible)

with open("./input.txt", "r") as f:
    contents = f.read().split("\n")

    # create a file tree

    root = Node(None, "/", {}, [])
    curr = root

    for line in contents:
        if not line.startswith("$"):
            key = line.split(" ")[0]
            val = line.split(" ")[1]

            if key == "dir":
                curr.directories[val] = Node(curr, val, {}, [])
            else:
                curr.files.append((int(key), val))
            continue

        command = line.split(" ")[1]
        if command == "cd":
            name = line.split(" ")[2]
            if name == "..":
                curr = curr.parent
            elif name in curr.directories:
                curr = curr.directories[name]
    print(root.solve())
    s = root.dir_size()
    print(smallest_deletable(root, MAX_SPACE - s))