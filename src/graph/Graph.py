class Graph:
    def __init__(self):
        self.num_nodes = 0
        self.graph_obj = dict()

    def add_vertex(self, node):
        self.graph_obj.update({node: []})
        self.num_nodes += 1

        pass

    def add_edge(self, node_1, node_2):
        self.graph_obj[node_1] = self.graph_obj[node_1] + [node_2]
        self.graph_obj[node_2] = self.graph_obj[node_2] + [node_1]
