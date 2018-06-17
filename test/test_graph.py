import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    """
    Test the graph structure containing the people and their transactions.
    """
    def test_add_person(self):
        """
        Test the success of adding a new person to the graph.
        """
        g = Graph()
        self.assertEqual(g.size(), 0)
        g.add_person("John")
        self.assertEqual(g.size(), 1)
        g.add_person("George")
        self.assertEqual(g.size(), 2)
        
    def test_add_person_exception(self):
        """
        Test that an exception is thrown when adding two people with the same
        name.
        """
        g = Graph()
        self.assertEqual(g.size(), 0)
        g.add_person("John")
        with self.assertRaises(ValueError):
            g.add_person("John")
