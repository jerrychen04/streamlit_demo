import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
from app import create_chart, get_data

class TestApp(unittest.TestCase):
    
    def test_create_chart(self):
        user_value = 2.5
        df = get_data(user_value)
        fig = create_chart(df, user_value)
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        expected_title = f'Chart for user input: {user_value}'
        self.assertEqual(ax.get_title(), expected_title)

if __name__ == "__main__":
    unittest.main()
