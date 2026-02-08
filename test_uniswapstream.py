# test_uniswapstream.py
"""
Tests for UniswapStream module.
"""

import unittest
from uniswapstream import UniswapStream

class TestUniswapStream(unittest.TestCase):
    """Test cases for UniswapStream class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UniswapStream()
        self.assertIsInstance(instance, UniswapStream)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UniswapStream()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
