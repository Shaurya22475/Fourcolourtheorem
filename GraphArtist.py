import networkx as nx
import matplotlib.pyplot as plt
import GraphGenerator
import geopandas as gpd

def draw_graph(mygraph, nodecolor):
    pos=nx.spring_layout(mygraph)
    nx.draw(mygraph, pos, with_labels=True, font_weight='bold', node_size=500, node_color=nodecolor, edge_color='gray')
    plt.title("Graph Model")
    # plt.gca().set_facecolor('#EFEFEF')
    plt.show()

def print_nodes(graph):
    print("Nodes in the graph:")
    for node in graph.nodes:
        print(node)

def set_color_keys(graph, keyColor):
    basecolors=[1,2,3,4]
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
    #print(keyColor)

def set_graph_color(graph, keyColor):
    ret_colors=[]
    colors=['salmon', 'gold', 'mediumaquamarine', 'steelblue']
    try:
        for vertices in graph.nodes:
            ret_colors.append(colors[keyColor[vertices]-1])
        return ret_colors
    except IndexError:
        print('Index out of range exception at colors[] in set_graph_color.')
        return

def mygraphmain(mygraph):
    #checking if graph is planar
    try:
        _ = nx.check_planarity(mygraph)
    except nx.NetworkXException:
        print("Graph Is Non-Planar")
        return

    keyColor={}
    set_color_keys(mygraph,keyColor)
    nodecolors = set_graph_color(mygraph, keyColor)
    draw_graph(mygraph, nodecolors)

mygraphmain(GraphGenerator.generateDodecahedron())
mygraphmain(GraphGenerator.generatePetersen())
mygraphmain(GraphGenerator.generateCubic())