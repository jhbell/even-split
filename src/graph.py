class Graph():
    """
    The graph data structure for storing people and their transactions
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

    def add_person(self, name: str):
        """
        Add a new person to the graph. This is equivalent to adding
        a new node.
        """
        if name in self.container:
            raise ValueError("Name already exists!")
        self.container[name] = []
