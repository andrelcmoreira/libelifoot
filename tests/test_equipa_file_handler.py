from unittest.mock import patch

from libelifoot.dto.color import Color
from libelifoot.dto.equipa import Equipa
from libelifoot.file.equipa import EquipaFileHandler


@patch('libelifoot.parser.equipa.EquipaParser.parse')
def test_read_equipa(mock_parse):
    equipa = Equipa(ext_name='FORTALEZA EC', short_name='FORTALEZA',
                    country='BRA', level=10,
                    colors=Color(text=b'', background=b''),
                    coach='Juan Pablo Vojvoda', players=[])

    mock_parse.return_value = equipa

    assert EquipaFileHandler.read('FORTALEZA.EFT') == equipa

    mock_parse.assert_called_once()
