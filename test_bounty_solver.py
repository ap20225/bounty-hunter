import unittest
from bounty_solver import solve_bounty, calculate_reward

class TestBountySolver(unittest.TestCase):
    def test_solve_bounty(self):
        result = solve_bounty(100)
        self.assertEqual(result, "Bounty of $100 solved successfully!")
    
    def test_calculate_reward(self):
        result = calculate_reward(50, 2)
        self.assertEqual(result, 100)
    
    def test_calculate_reward_default_difficulty(self):
        result = calculate_reward(75)
        self.assertEqual(result, 75)
