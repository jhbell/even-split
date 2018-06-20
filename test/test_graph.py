import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    """
    Test the graph structure containing the people and their transactions.
    """
    def test_add_node_size(self):
        """
        Test the success of adding a new node to the graph using the size
        of the graph.
        """
        g = Graph()
        self.assertEqual(g.size(), 0)
        g.add_node("A")
        self.assertEqual(g.size(), 1)
        g.add_node("B")
        self.assertEqual(g.size(), 2)

    def test_add_node_str(self):
        """
        Test the success of adding a new node to the graph using
        the string representation of the graph.
        """
        correct = "{'A': {}, 'B': {}, 'C': {}}"
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_node("C")
        self.assertEqual(str(g), correct)

    def test_repr(self):
        """
        Test the correctness of the __repr__ function.
        """
        correct = "{'A': {}, 'B': {}, 'C': {}}"
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_node("C")
        self.assertEqual(repr(g), correct)
        
    def test_add_node_duplicate(self):
        """
        Test that an exception is thrown when adding two nodes with the same
        name.
        """
        g = Graph()
        self.assertEqual(g.size(), 0)
        g.add_node("A")
        with self.assertRaises(ValueError):
            g.add_node("A")

    def test_add_edge_default(self):
        """
        Test adding an edge to the graph.
        """
        correct = "{'A': {'B': 0.0}, 'B': {}}"
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_edge("A", "B")
        self.assertEqual(str(g), correct)

    def test_add_edge_with_value(self):
        """
        Test adding an edge to the graph.
        """
        correct = "{'A': {'B': 22.22}, 'B': {}}"
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_edge("A", "B", 22.22)
        self.assertEqual(str(g), correct)

    def test_add_edge_invalid_start(self):
        """
        Test adding an edge where the start node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.add_edge("C", "B")
        self.assertIn("start", str(context.exception))

    def test_add_edge_invalid_end(self):
        """
        Test adding an edge where the end node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.add_edge("A", "C")
        self.assertIn("end", str(context.exception))

    def test_get_weight(self):
        """
        Test getting the weight of an edge between two nodes.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_edge("A", "B", 123.45)
        self.assertEqual(g.get_weight("A", "B"), 123.45)

    def test_get_weight_invalid_start(self):
        """
        Test getting the weight of an edge where the start node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.get_weight("C", "B")
        self.assertIn("start", str(context.exception))

    def test_get_weight_invalid_end(self):
        """
        Test getting the weight of an edge where the end node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.get_weight("A", "C")
        self.assertIn("end", str(context.exception))

    def test_get_weight_no_edge(self):
        """
        Test getting the weight of an edge that does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.get_weight("A", "B")
        self.assertIn("edge", str(context.exception))

    def test_set_weight(self):
        """
        Test setting the weight of an edge between two nodes.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_edge("B", "A")
        self.assertEqual(g.get_weight("B", "A"), 0.0)
        g.set_weight("B", "A", 123.45)
        self.assertEqual(g.get_weight("B", "A"), 123.45)

    def test_set_weight_invalid_start(self):
        """
        Test setting the weight of an edge where the start node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.set_weight("C", "B", 20.00)
        self.assertIn("start", str(context.exception))

    def test_set_weight_invalid_end(self):
        """
        Test setting the weight of an edge where the end node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.set_weight("A", "C", 44.43)
        self.assertIn("end", str(context.exception))

    def test_set_weight_no_edge(self):
        """
        Test setting the weight of an edge that does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.set_weight("A", "B", 1.51)
        self.assertIn("edge", str(context.exception))


    def test_add_weight(self):
        """
        Test updating the weight of an edge between two nodes.
        """
        correct = "{'A': {'B': 3.14}, 'B': {}}"
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_edge("A", "B")
        g.add_weight("A", "B", 3.14)
        self.assertEqual(str(g), correct)

    def test_add_weight_invalid_start(self):
        """
        Test addting the weight of an edge where the start node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.add_weight("C", "B", 20.00)
        self.assertIn("start", str(context.exception))

    def test_add_weight_invalid_end(self):
        """
        Test addting the weight of an edge where the end node does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.add_weight("A", "C", 44.43)
        self.assertIn("end", str(context.exception))

    def test_add_weight_no_edge(self):
        """
        Test addting the weight of an edge that does not exist.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        with self.assertRaises(ValueError) as context:
            g.add_weight("A", "B", 1.51)
        self.assertIn("edge", str(context.exception))

    def test_iter(self):
        """
        Test iteration over the graph. This should iterate over the nodes
        of the graph.
        """
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        g.add_node("C")
        g.add_node("D")
        i = iter(g)
        self.assertEqual(next(i), "A")
        self.assertEqual(next(i), "B")
        self.assertEqual(next(i), "C")
        self.assertEqual(next(i), "D")

