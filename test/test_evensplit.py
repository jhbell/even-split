import unittest
from src.evensplit import EvenSplit

class TestEvenSplit(unittest.TestCase):
    """
    Test the EvenSplit program which actually divides up payments and produces
    a result.
    """
    def test_add_person(self):
        """
        Test that people are added properly to the internal graph.
        """
        correct = "{'John': {'Sara': 0.0}, 'Sara': {'John': 0.0}}"
        es = EvenSplit()
        es.add_person("John")
        es.add_person("Sara")
        self.assertEqual(es.count(), 2)
        self.assertEqual(str(es), correct)

    def test_add_person_none(self):
        """
        Test that an exception is raised when adding a person with None as
        the name.
        """
        es = EvenSplit()
        with self.assertRaises(ValueError):
            es.add_person(None)

    def test_repr(self):
        """
        Test the correctness of the __repr__ function.
        """
        correct = "{'John': {'Sara': 0.0}, 'Sara': {'John': 0.0}}"
        es = EvenSplit()
        es.add_person("John")
        es.add_person("Sara")
        self.assertEqual(repr(es), correct)


