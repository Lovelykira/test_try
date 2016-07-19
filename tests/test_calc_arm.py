import unittest
from mock import Mock, patch, sentinel
from app.solder import Solder

class TestSolder(unittest.TestCase):
    def setUp(self):
        self.solder = Solder()

    def test_calc_armor(self):
        self.solder._experience = 2
        self.assertEqual(self.solder.calc_armor(), 0.07)

    @patch('app.solder.random')
    def test_get_power(self, mock_random):
        mock_random.randint = Mock(return_value=5)

        self.solder._health=100
        self.assertEqual(self.solder.get_power(), 2.525)

    def test_do_attack(self):
        self.solder._health = 100

        with patch.object(self.solder, 'get_power') as mock_get_power:
            mock_get_power.return_value = sentinel.get_power
            self.assertEqual(self.solder.do_attack(), sentinel.get_power)
