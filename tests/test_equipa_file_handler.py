from unittest import mock

from fixtures import mock_equipa, mock_equipa_bytes


def test_read_equipa(mock_equipa, mock_equipa_bytes):
    pass # TODO


@mock.patch('libelifoot.infrastructure.eft.serializer.equipa.EquipaSerializer.serialize')
def test_write_equipa(mock_serialize, mock_equipa):
    pass # TODO
