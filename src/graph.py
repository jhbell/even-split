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
        for node in self.container:
            if node != name:
                self.container[node][name] = 0.0
                self.container[name][node] = 0.0

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

