from unittest.mock import patch

from fixtures import mock_equipa

from libelifoot.api import view_equipa


def test_view_equipa(mock_equipa):
    file = 'FORTALEZA.EFT'

    with patch(
        'libelifoot.file.equipa.EquipaFileHandler.read',
        return_value=mock_equipa
    ) as mock_read:
        cmd = view_equipa.Cmd(file)

        assert cmd.run() == mock_equipa
        mock_read.assert_called_once_with(file)
