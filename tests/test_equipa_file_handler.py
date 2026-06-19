from unittest import mock

from fixtures import mock_equipa, mock_equipa_bytes

from libelifoot.file.equipa import EquipaFileHandler


def test_read_equipa(mock_equipa, mock_equipa_bytes):
    with mock.patch(
        'builtins.open',
        mock.mock_open(read_data=bytes(mock_equipa_bytes))
    ) as mock_file:
        with mock.patch(
            'libelifoot.parser.equipa.EquipaParser.parse',
            return_value=mock_equipa
        ) as mock_parse:
            assert EquipaFileHandler.read('FORTALEZA.EFT') == mock_equipa

            mock_file.assert_called_once_with('FORTALEZA.EFT', 'rb')
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
