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
        g.add_node("John")
        self.assertEqual(g.size(), 1)
        g.add_node("George")
        self.assertEqual(g.size(), 2)

    def test_add_node_str(self):
        """
        Test the success of adding a new node to the graph using
        the string representation of the graph.
        """
        correct = ("{'John': {'George': 0.0, 'Jamie': 0.0}, 'George': "
                   "{'John': 0.0, 'Jamie': 0.0}, 'Jamie': {'John': 0.0, "
                   "'George': 0.0}}")
        g = Graph()
        g.add_node("John")
        g.add_node("George")
        g.add_node("Jamie")
        self.assertEqual(str(g), correct)
        
    def test_add_node_value_error(self):
        """
        Test that an exception is thrown when adding two nodes with the same
        name.
        """
        g = Graph()
        self.assertEqual(g.size(), 0)
        g.add_node("John")
        with self.assertRaises(ValueError):
            g.add_node("John")

    def test_add_weight(self):
        """
        Test updating the weight of an edge between two nodes.
        """
        correct = "{'Matt': {'Amy': 3.14}, 'Amy': {'Matt': 0.0}}"
        g = Graph()
        g.add_node("Matt")
        g.add_node("Amy")
        g.add_weight("Matt", "Amy", 3.14)
        self.assertEqual(str(g), correct)


