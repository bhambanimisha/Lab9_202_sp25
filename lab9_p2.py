def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        current = queue.pop(0)

        if current not in visited:
            visited.append(current)

            # Enqueue neighbors in sorted numerical order
            for neighbor in sorted(graph[current]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited
