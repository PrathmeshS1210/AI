#A*

class Node:
    def __init__(self, data, level, parent=None):
        self.data = data
        self.level = level
        self.parent = parent
        self.fval = self.level + sum(a != b and a != '_' for r1, r2 in zip(data, goal) for a, b in zip(r1, r2))

    def children(self):
        x, y = [(i, r.index('_')) for i, r in enumerate(self.data) if '_' in r][0]
        moves = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        kids = []
        for i,j in moves:
            if 0<=i<3 and 0<=j<3:
                new = [r[:] for r in self.data]
                new[x][y], new[i][j] = new[i][j], new[x][y]
                kids.append(Node(new, self.level+1, self))
        return kids

def solve(start, goal_state):
    global goal
    goal = goal_state
    open = [Node(start, 0)]
    seen = set()
    while open:
        node = open.pop(0)
        if node.data == goal:
            path = []
            while node: path.append(node); node = node.parent
            for i, n in enumerate(reversed(path)):
                print(f"\nStep {i}:"); [print(' '.join(r)) for r in n.data]
            return
        seen.add(str(node.data))
        for c in node.children():
            if str(c.data) not in seen:
                open.append(c)
        open.sort(key=lambda x: x.fval)

def get_input(name):
    print(f"Enter {name} state (use '_' for blank):")
    return [input().split() for _ in range(3)]

start = get_input("start")
goal = get_input("goal")
solve(start, goal)

# Output: 
# Enter start state (use '_' for blank):
# 1 2 3
# 4 _ 5
# 7 8 6 
# Enter goal state (use '_' for blank):
# 1 2 3
# 4 5 6
# 7 8 _ 
