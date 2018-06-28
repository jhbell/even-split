from src.graph import Graph

class EvenSplit():
    """
    The EvenSplit class contains the code which handles adding people,
    transactions, and reducing the graph into the minimum number of
    transactions.
    """
    def __init__(self):
        """
        Construct a new EvenSplit instance.
        """
        self.graph = Graph()

    def __str__(self):
        """
        Return a string form of the EvenSplit object. This is the same as
        using the internal graph's __str__ function.
        """
        return str(self.graph)

    def __repr__(self):
        """
        Return a human-readable string form of the EvenSplit object. This is
        the same as using the internal graph's __repr__ function.
        """
        return repr(self.graph)

    def add_person(self, name: str):
        """
        Add a new person to the EvenSplit object. This adds a new node for the
        given name and connects it to all other nodes within the graph,
        excluding itself.
        """
        if name is None:
            raise ValueError("Name cannot be None!")
        self.graph.add_node(name)
        for person in self.graph:
            if person != name:
                self.graph.add_edge(name, person)
                self.graph.add_edge(person, name)

    def add_transaction(self, name: str, amount: float):
        """
        Add a transaction and evenly split the amount across all people.
        """
        split_amount = amount / self.count()
        for person in self.graph:
            if person != name:
                self.graph.add_weight(person, name, split_amount)

    def count(self):
        """
        Return the number of people in the graph.
        """
        return self.graph.size()
