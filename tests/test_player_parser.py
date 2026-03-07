from fixtures import mock_equipa, mock_players, mock_equipa_bytes

from libelifoot.parser.player import PlayersParser
from libelifoot.util.offset import OffsetCalculator


def test_parse_players(mock_equipa, mock_players, mock_equipa_bytes):
    ext_len = len(mock_equipa.ext_name)
    short_len = len(mock_equipa.short_name)

    players_offs = OffsetCalculator.get_players(ext_len, short_len)
    count_offs = OffsetCalculator.get_players_number(ext_len, short_len)

    parser = PlayersParser(mock_equipa_bytes, players_offs, count_offs)
    players = parser.parse()

    assert players == mock_players
