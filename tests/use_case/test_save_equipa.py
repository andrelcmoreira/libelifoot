from unittest.mock import MagicMock, patch

from libelifoot.use_case.save_equipa import SaveEquipa


def test_save_equipa(mock_equipa, mock_equipa_bytes):
    file_name = 'FORTALEZA.EFT'
    repo_mock = MagicMock()

    with patch(
        'libelifoot.infrastructure.eft.serializer.equipa.EquipaSerializer.serialize',
        return_value=mock_equipa_bytes
    ) as mock_serialize:
        cmd = SaveEquipa(file_name, mock_equipa, repo_mock)

        cmd.run()

        mock_serialize.assert_called_once_with(mock_equipa)
        repo_mock.save.assert_called_once_with(file_name, mock_equipa_bytes)
