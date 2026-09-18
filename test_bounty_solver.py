import unittest
from bounty_solver import solve_bounty

class TestBountySolver(unittest.TestCase):
    def test_solve_bounty_basic(self):
        """Test basic bounty solving functionality."""
        result = solve_bounty(100, 50)
        self.assertEqual(result, 150)
    
    def test_solve_bounty_zero(self):
        """Test bounty solving with zero values."""
        result = solve_bounty(0, 0)
        self.assertEqual(result, 0)
    
    def test_solve_bounty_negative(self):
        """Test bounty solving with negative values."""
        result = solve_bounty(-10, -5)
        self.assertEqual(result, -15)

if __name__ == '__main__':
    unittest.main()