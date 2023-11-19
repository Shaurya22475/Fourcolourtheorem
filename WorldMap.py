import networkx as nx
import matplotlib.pyplot as plt
import geopandas as gpd

def worldmap():
    # Load a world map dataset
    world = gpd.read_file("/Users/nishchayaroy/Desktop/world/world.geojson")

    # Create a graph
    G = nx.Graph()

    # Add nodes for each country
    for idx, country in world.iterrows():
        G.add_node(country['NAME'])

    # Add edges for neighboring countries
    for idx, country in world.iterrows():
        neighbors = world[world.geometry.touches(country['geometry'])]
        for neighbor in neighbors.itertuples():
            G.add_edge(country['NAME'], neighbor.NAME)
    return(G)

def draw_graph(mygraph, nodecolor):
    #pos=nx.spring_layout(mygraph)
    world2 = gpd.read_file("/Users/nishchayaroy/Desktop/world/world.geojson")
    pos = {country['NAME']: (country.geometry.centroid.x, country.geometry.centroid.y) for idx, country in world2.iterrows()}
    nx.draw(mygraph, pos, with_labels=True, font_weight='bold', node_size=500, node_color=nodecolor, edge_color='gray')
    plt.title("Graph Model")
    plt.show()

def print_nodes(graph):
    print("Nodes in the graph:")
    for node in graph.nodes:
        print(node)

def set_color_keys(graph):
    basecolors=[1,2,3,4]
    keyColor={}
    #inititalizing the key-colour relation and setting it to zero
    for i in graph.nodes:
        keyColor[i]=0

    #getting color keys of all the neighbours
    for i in graph.nodes:
        nbhcolors=[]
        for j in list(graph.neighbors(i)):
            nbhcolors.append(keyColor[j])            
        for color in basecolors:
            if color not in nbhcolors:
                keyColor[i] = color
                break
    return keyColor

def set_graph_color(graph, keyColor):
    ret_colors=[]
    colors=['salmon', 'gold', 'mediumaquamarine', 'steelblue']
    for vertices in graph.nodes:
        ret_colors.append(colors[keyColor[vertices]-1])
    return ret_colors


def mygraphmain(mygraph):
    #checking if graph is planar
    try:
        _ = nx.check_planarity(mygraph)
    except nx.NetworkXException:
        print("Graph Is Non-Planar")
        return
    keyColor=set_color_keys(mygraph)
    set_color_keys(mygraph)
    nodecolors = set_graph_color(mygraph, keyColor)
    draw_graph(mygraph, nodecolors)

mygraphmain(worldmap())