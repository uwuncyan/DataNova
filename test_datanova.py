# test_datanova.py
"""
Tests for DataNova module.
"""

import unittest
from datanova import DataNova

class TestDataNova(unittest.TestCase):
    """Test cases for DataNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataNova()
        self.assertIsInstance(instance, DataNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
