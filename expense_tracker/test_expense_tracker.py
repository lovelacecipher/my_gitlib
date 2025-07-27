import unittest
import os
import json
from expense_tracker import save_expenses, load_expenses, view_total, filter_expenses

class TestExpenseTracker(unittest.TestCase):
  
  def setUp(self):
    """Run before each test:create a temporary test file."""
    self.test_file = "test_expenses.json"
    self.sample_expenses = [
      {"date": "2025-07-25", "category": "Food", "amount": 10.5, "description": "Lunch"},
      {"date": "2025-07-26", "category": "Transport", "amount": 5.0, "description": "Bus ticket"},
      {"date": "2025-07-26", "category": "Food", "amount": 15.0, "description": "Dinner"}
    ]
    with open(self.test_file, "w") as f:
      json.dump(self.sample_expenses, f, indent=4)

  def tearDown(self):
    """Run after each test: clean up the test file."""
    if os.path.exists(self.test_file):
      os.remove(self.test_file)

  def test_load_expenses(self):
    """Check if expenses load correctly."""
    with open(self.test_file, "w") as f:
      json.dump(self.sample_expenses, f)
    loaded = load_expenses()
    self.assertEqual(len(loaded, 3))
    self.assertEqual(loaded[1]['amount'], 5.0)

  def test_total_spent(self):
    """Check if total spent calculation is correct."""
    total = sum(e['amount'] for e in self.sample_expenses)
    self.assertAlmostEqual(total, 30.5, places=2)

  def test_filter_expenses(self):
    """Check filtering by category."""
    food_expenses = [e for e in self.sample_expenses if e['category'] == "Food"]
    self.assertEqual(len(food_expenses), 2)
    self.assertTrue(all(e['category'] == "Food" for e in food_expenses))

if __name__ == "__main__":
  unittest.main()