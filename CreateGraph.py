import json

from pyvis.network import Network

file = "./graph.json"

def get_data():
    with open(file, "r") as json_file:
        return json.load(json_file)

def map_data(data):
    g = Network(height="800px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    for node in data["nodes"]:
        g.add_node(node)
    for edge in data["edges"]:
        g.add_edge(*edge)

    g.show("graph.html")

if __name__ == '__main__':
    data = get_data()
    map_data(data)
