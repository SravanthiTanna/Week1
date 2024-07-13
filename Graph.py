Graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
    node = input(f"Enter node{i + 1}: ")
    adj_nodes = int(input("Enter number of adjacent nodes: "))
    adj_list = []  # Initialize the list for adjacent nodes here
    for j in range(adj_nodes):
        adj_node = input(f"Enter adjacent node{j + 1}: ")
        adj_list.append(adj_node)  # Append each adjacent node to the list
    Graph[node] = adj_list  # Assign the list to the node after the inner loop

wanted_node = input("Enter the node to display its adjacent nodes: ")
print(f"Adjacent nodes of {wanted_node} are: {Graph[wanted_node]}")
