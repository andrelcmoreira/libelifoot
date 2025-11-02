from unittest import mock

from fixtures import mock_equipa

from libelifoot.file.equipa import EquipaFileHandler


def test_read_equipa(mock_equipa):
    with mock.patch(
        'libelifoot.parser.equipa.EquipaParser.parse',
        return_value=mock_equipa
    ) as mock_parse:
        assert EquipaFileHandler.read('FORTALEZA.EFT') == mock_equipa

        mock_parse.assert_called_once()


@mock.patch('libelifoot.serializer.equipa.EquipaSerializer.serialize')
def test_write_equipa(mock_serialize, mock_equipa):
    file_path = 'FORTALEZA.EFT'
    serialized_equipa = b'\x00\x01\x02\x03\x04\x05'

    mock_serialize.return_value = serialized_equipa

    with mock.patch('builtins.open', mock.mock_open()) as mock_file:
        EquipaFileHandler.write(file_path, mock_equipa)

        mock_file.assert_called_once_with(file_path, 'wb')
        mock_serialize.assert_called_once_with(mock_equipa)
        mock_file().write.assert_called_once_with(serialized_equipa)
