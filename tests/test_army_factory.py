import pytest
from mock import patch

from app.army_factory import ArmyFactory
@patch('app.army_factory.choice', return_value=5)
def test_create(mock_choice, fixt_test_strategy):
    army = ArmyFactory.create(fixt_test_strategy)

    assert army.get_alive_squads() == army._squads
    assert len(army._squads) == 5