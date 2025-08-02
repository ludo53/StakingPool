# test_stakingpool.py
"""
Tests for StakingPool module.
"""

import unittest
from stakingpool import StakingPool

class TestStakingPool(unittest.TestCase):
    """Test cases for StakingPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StakingPool()
        self.assertIsInstance(instance, StakingPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StakingPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
