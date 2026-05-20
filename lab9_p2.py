 # Create empty visited list
    # # Create queue initialized with start node
    # While queue is not empty:
    #   Dequeue current node
    #   If not visited:
    #   Add to visited
    #   For each neighbor of current node (in sorted order):
    #     If not visited and not in queue:
    #         Enqueue neighbor
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
            for neighbor in sorted(graph[current_node]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited
