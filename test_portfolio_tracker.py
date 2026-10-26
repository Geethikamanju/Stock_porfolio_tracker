"""
Unit tests for portfolio_tracker.py
"""

import os
import unittest
from portfolio_tracker import (
    STOCK_PRICES,
    calculate_portfolio_breakdown,
    save_to_csv,
    save_to_txt,
)


class TestPortfolioTracker(unittest.TestCase):
    def setUp(self):
        self.sample_holdings = {
            "AAPL": 10,
            "TSLA": 5,
        }
        self.sample_prices = {
            "AAPL": 180.0,
            "TSLA": 250.0,
        }
        self.test_txt = "test_portfolio.txt"
        self.test_csv = "test_portfolio.csv"

    def tearDown(self):
        for path in (self.test_txt, self.test_csv):
            if os.path.exists(path):
                os.remove(path)

    def test_calculation(self):
        breakdown, total = calculate_portfolio_breakdown(
            self.sample_holdings, self.sample_prices
        )
        # 10 * 180.0 = 1800.0
        # 5 * 250.0 = 1250.0
        # Total = 3050.0
        self.assertEqual(len(breakdown), 2)
        self.assertAlmostEqual(total, 3050.0, places=2)
        self.assertEqual(breakdown[0]["ticker"], "AAPL")
        self.assertAlmostEqual(breakdown[0]["subtotal"], 1800.0, places=2)
        self.assertEqual(breakdown[1]["ticker"], "TSLA")
        self.assertAlmostEqual(breakdown[1]["subtotal"], 1250.0, places=2)

    def test_empty_holdings(self):
        breakdown, total = calculate_portfolio_breakdown({}, self.sample_prices)
        self.assertEqual(len(breakdown), 0)
        self.assertEqual(total, 0.0)

    def test_save_to_txt(self):
        breakdown, total = calculate_portfolio_breakdown(
            self.sample_holdings, self.sample_prices
        )
        saved_path = save_to_txt(breakdown, total, filename=self.test_txt)
        self.assertTrue(os.path.exists(saved_path))
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("AAPL", content)
            self.assertIn("TSLA", content)
            self.assertIn("3050.00", content)

    def test_save_to_csv(self):
        breakdown, total = calculate_portfolio_breakdown(
            self.sample_holdings, self.sample_prices
        )
        saved_path = save_to_csv(breakdown, total, filename=self.test_csv)
        self.assertTrue(os.path.exists(saved_path))
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("AAPL,10,180.00,1800.00", content)
            self.assertIn("TSLA,5,250.00,1250.00", content)
            self.assertIn("TOTAL INVESTMENT,,,3050.00", content)


if __name__ == "__main__":
    unittest.main()
