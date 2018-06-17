class Graph():
    """
    The graph data structure for storing people and their transactions.
    """
    def __init__(self):
        """
        Construct a new graph using a dict as a container.
        """
        self.container = dict()

    def size(self):
        """
        Return the number of people in the graph. This is equivalent to
        the number of ndoes in the graph.
        """
        return len(self.container)

    def add_node(self, name: str):
        """
        Add a new person to the graph. This is equivalent to adding
        a new node. This node will be connected to all other nodes by an
        edge with weight zero.
        """
        if name in self.container:
            raise ValueError("Name already exists!")
        self.container[name] = dict()

    def add_edge(self, start: str, end: str, weight: float=0.0):
        """
        Add a new edge from start to end, optionally with the given weight.
        """
        if start not in self.container:
            raise ValueError("The provided start node does not exist!")
        if end not in self.container:
            raise ValueError("The provided end node does not exist!")
        self.container[start][end] = weight

    def get_weight(self, start: str, end: str):
        """
        Get the weight of the edge from start to end.
        """
        if start not in self.container:
            raise ValueError("The provided start node does not exist!")
        if end not in self.container:
            raise ValueError("The provided end node does not exist!")
        if end not in self.container[start]:
            raise ValueError(
                    "There is no edge from {} to {}".format(start, end))
        return self.container[start][end]

    def add_weight(self, start: str, end: str, amount: float):
        """
        Add weight to the edge that goes from start to end.
        """
        self.container[start][end] = self.container[start][end] + amount

    def __str__(self):
        """
        Print the contents of the graph. This prints the contents of
        self.container
        """
        return str(self.container)

