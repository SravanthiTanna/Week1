from collections import deque
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []  
    while queue:
        current_node = queue.popleft()  
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)  
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)  
    print(" -> ".join(traversal_order))
def main():
    Graph = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = input(f"Enter node {i + 1}: ")
        adj_nodes = int(input("Enter number of adjacent nodes: "))
        adj_list = []
        for j in range(adj_nodes):
            adj_node = input(f"Enter adjacent node {j + 1}: ")
            adj_list.append(adj_node)
        Graph[node] = adj_list
    start_node = input("Enter the starting node for BFS traversal: ")
    print("BFS Traversal: ", end="")
    bfs(Graph, start_node)
if __name__ == "__main__":
    main()
