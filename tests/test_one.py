import unittest
from app.views import mul


class TestOne(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(2,3),6)