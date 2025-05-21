graph_3 = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {5: 3},
    4: {5: 1},
    5: {}
}

import heapq

def dijkstra(graph, start):
    # Distance from start to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: (distance_so_far, current_node)
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Skip if we’ve already found a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

