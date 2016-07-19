from mock import patch, sentinel

from app.army import Army
from app.squad import Squad


def test_take_damage():
    army = Army()
    squad = Squad()
    army.add_group(squad)

    with patch.object(squad, 'take_damage') as mock_take_damage:
        army.take_damage(sentinel.dmg)
        mock_take_damage.assert_called_once_with(sentinel.dmg)