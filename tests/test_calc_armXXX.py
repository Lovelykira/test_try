import pytest

from mock import Mock, patch, sentinel
from app.solder import Solder


@pytest.fixture
def fixt_soldier():
    return Solder()


def test_calc_armor(fixt_soldier):
    fixt_soldier._experience = 2

    assert fixt_soldier.calc_armor() == 0.07

@patch('app.solder.random')
def test_get_power(mock_random, fixt_soldier):
    mock_random.randint.return_value = 5
    fixt_soldier._health = 100

    assert fixt_soldier.get_power() == 2.525

def test_do_attack(fixt_soldier):
    fixt_soldier._health = 100

    with patch.object(fixt_soldier, 'get_power') as mock_get_power:
        mock_get_power.return_value = sentinel.get_power
        assert fixt_soldier.do_attack() == sentinel.get_power
