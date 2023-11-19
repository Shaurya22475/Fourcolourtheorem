import networkx as nx

def generateDodecahedron():
    G = nx.Graph()
    #adding Vertices
    vertices = range(1, 20)
    G.add_nodes_from(vertices)
    #adding edges
    edges = [ (1,8), (1,2), (1,5), (2,3), (2,10), (3,12), (3,4), (4,14), (4,14), (5,6), (6,7), (6,15), (7,8), (7,17), (8,9), (9,10), (9,18), (10,11), (11,12), (11,19), (12,13), (13,14), (13,20), (13,15), (15,16), (16, 17), (16,20), (17,18), (18,19), (19,20) ]
    G.add_edges_from(edges)
    return G

def generatePetersen():
    return nx.petersen_graph()

def generateCubic():
    return nx.cubical_graph()