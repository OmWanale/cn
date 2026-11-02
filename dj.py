import heapq

# Step 1: Define network topology
network = {
    'A': {'B': 2, 'C': 5, 'D': 4},
    'B': {'A': 2, 'C': 3, 'D': 2, 'E': 6},
    'C': {'A': 5, 'B': 3, 'D': 1, 'E': 4},
    'D': {'A': 4, 'B': 2, 'C': 1, 'E': 2},
    'E': {'B': 6, 'C': 4, 'D': 2}
}

# Step 2: Implement Dijkstra's algorithm
def dijkstra(graph, source):
    distances = {router: float('inf') for router in graph}
    previous = {router: None for router in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_router = heapq.heappop(priority_queue)

        if current_distance > distances[current_router]:
            continue

        for neighbor, cost in graph[current_router].items():
            new_distance = current_distance + cost

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_router
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, previous

# Step 3: Construct shortest path
def get_path(previous, source, destination):
    path = []

    while destination is not None:
        path.append(destination)

        if destination == source:
            break

        destination = previous[destination]

    path.reverse()
    return path if path[0] == source else []

# Step 4: Display routing tables for all routers
print("========== DYNAMIC ROUTING TABLES ==========")

for source in network:
    distances, previous = dijkstra(network, source)
    print(f"\nRouter {source}:")

    for destination in network:
        if destination != source:
            path = get_path(previous, source, destination)
            print(f"To {destination} -> Path: {' -> '.join(path)}, Cost: {distances[destination]}")

# Step 5: Accept source and destination from user
source = input("\nEnter Source Router: ").upper()
destination = input("Enter Destination Router: ").upper()

# Step 6: Validate input and display shortest route
if source in network and destination in network:
    distances, previous = dijkstra(network, source)
    path = get_path(previous, source, destination)

    print("\nDynamic Route Found!")
    print(f"Source       : {source}")
    print(f"Destination  : {destination}")
    print(f"Shortest Path: {' -> '.join(path)}")
    print(f"Cost         : {distances[destination]}")
else:
    print("\nInvalid source or destination router.")