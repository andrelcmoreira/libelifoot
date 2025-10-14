from unittest.mock import patch

from fixtures import mock_equipa

from libelifoot.file.equipa import EquipaFileHandler


def test_read_equipa(mock_equipa):
    with patch(
        'libelifoot.parser.equipa.EquipaParser.parse',
        return_value=mock_equipa
    ) as mock_parse:
        assert EquipaFileHandler.read('FORTALEZA.EFT') == mock_equipa

        mock_parse.assert_called_once()
