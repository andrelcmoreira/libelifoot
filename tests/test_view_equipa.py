from unittest.mock import patch

from fixtures import mock_equipa

from libelifoot.api.view_equipa import view


def test_view_equipa(mock_equipa):
    file = 'FORTALEZA.EFT'

    with patch(
        'libelifoot.file.equipa.EquipaFileHandler.read',
        return_value=mock_equipa
    ) as mock_read:
        assert view(file) == mock_equipa

        mock_read.assert_called_once_with(file)
