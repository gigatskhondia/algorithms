class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def dfs(graph, start_node, end_node):
    frontier = Stack()
    frontier.push(start_node)
    explored = set()
    while frontier:
        current_node = frontier.pop()
        if current_node in explored:
            continue
        if current_node == end_node:
            return "success"

        for neighbor in graph.get_neigbhors(current_node):  # TODO
            frontier.push(neighbor)
        explored.add(current_node)
