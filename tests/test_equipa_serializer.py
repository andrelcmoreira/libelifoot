from fixtures import mock_equipa, mock_equipa_bytes

from libelifoot.serializer.equipa import EquipaSerializer


def test_serialize_none_equipa():
    ret = EquipaSerializer.serialize(None)

    assert ret is None


def test_serialize_valid_equipa(mock_equipa, mock_equipa_bytes):
    ret = EquipaSerializer.serialize(mock_equipa)

    assert ret == mock_equipa_bytes
