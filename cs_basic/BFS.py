from queue import Queue


def bfs(graph, start_node, end_node):
    frontier = Queue()
    frontier.put(start_node)
    explored = set()

    while frontier:
        current_node = frontier.get()
        if current_node in explored:
            continue
        if current_node == end_node:
            return "success"

        for neighbor in graph.get_neigbhors(current_node):  # TODO
            frontier.put(neighbor)
        explored.add(current_node)
