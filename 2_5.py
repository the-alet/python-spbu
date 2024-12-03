from collections import deque

def water_jug_solver(M, N, K):
    # To store visited states
    visited = set()
    # Queue for BFS
    queue = deque()
    # Start with both jugs empty
    queue.append((0, 0, []))  # (jug1, jug2, path)

    while queue:
        jug1, jug2, path = queue.popleft()

        # If we reach the goal, return the path
        if jug1 == K:
            return path

        # If this state is already visited
        if (jug1, jug2) in visited:
            continue

        # Mark this state as visited
        visited.add((jug1, jug2))

        # Possible actions
        # Fill Jug1 from the pump
        if jug1 < M:
            queue.append((M, jug2, path + [(M, jug2)]))
        # Empty Jug2
        if jug2 > 0:
            queue.append((jug1, 0, path + [(jug1, 0)]))
        # Pour Jug1 to Jug2
        pour_to_jug2 = min(jug1, N - jug2)
        if pour_to_jug2 > 0:
            queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2, path + [(jug1 - pour_to_jug2, jug2 + pour_to_jug2)]))

    return "No solution found"

# Example usage
M = int(input("Enter the capacity of jug1: "))  # Capacity of jug1
N = int(input("Enter the capacity of jug2: "))  # Capacity of jug2
K = int(input("Enter the target volume: "))  # Target volume

solution = water_jug_solver(M, N, K)
if solution != "No solution found":
    print("Steps to achieve the target:")
    for step in solution:
        print(f"Jug1: {step[0]} gallons, Jug2: {step[1]} gallons")
else:
    print(solution)