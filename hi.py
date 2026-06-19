 import networkx as nx

# Graph creation
G = nx.Graph()

cities = ["EKM","ALP","KTM","IDK","TSR","PKD","MLP"]
roads = [
("EKM","ALP"),
("EKM","KTM"),
("KTM","IDK"),
("ALP","TSR"),
("TSR","PKD"),
("PKD","MLP"),
("IDK","TSR")
]

G.add_nodes_from(cities)
G.add_edges_from(roads)

# Connectivity
print("Is Connected:", nx.is_connected(G))

# Articulation Points
print("Articulation Points:", list(nx.articulation_points(G)))

# Bridges
print("Bridges:", list(nx.bridges(G)))

# Adjacency Matrix
print("Adjacency Matrix:")
print(nx.adjacency_matrix(G).todense())

# Incidence Matrix
print("Incidence Matrix:")
print(nx.incidence_matrix(G).todense())