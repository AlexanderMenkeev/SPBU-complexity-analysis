import networkx as nx
import random


def generate_strong_graph(numberOfNodes, numberOfEdges):
    nodes = list(range(0, numberOfNodes))
    S, T = set(nodes), set()

    if numberOfEdges > numberOfNodes * (numberOfNodes - 1):
        print("Too many edges!")

    # Pick a random node, and mark it as visited and the current node.
    current_node = random.sample(sorted(S), 1).pop()
    S.remove(current_node)
    T.add(current_node)

    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)

    # Create a random directed strongly connected graph.
    while S:
        # Randomly pick the next node from the neighbors of the current node.
        neighbor_node = random.sample(nodes, 1).pop()
        # If the new node hasn't been visited, add the edge from current to new.
        if neighbor_node not in T:
            graph.add_edge(current_node, neighbor_node, weight=random.randint(0, 1000))
            graph.add_edge(neighbor_node, current_node, weight=random.randint(0, 1000))
            S.remove(neighbor_node)
            T.add(neighbor_node)
        # Set the new node as the current node.
        current_node = neighbor_node

    while len(graph.edges) < numberOfEdges:
        [u, v] = tuple(random.sample(sorted(graph.nodes), 2))
        graph.add_edge(u, v, weight=random.randint(0, 1000))

    return graph


count = 1
for i in range(100, 1600, 50):
    test_graph = generate_strong_graph(i, int(i * (i - i * 0.5)))
    nx.write_edgelist(test_graph, "graph" + str(count))
    count += 1
    print(i)
