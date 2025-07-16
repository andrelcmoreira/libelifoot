from libelifoot.serializer.coach import CoachSerializer


def test_serialize_none_coach():
    ret = CoachSerializer.serialize(None)

    assert ret is None


def test_serialize_empty_coach():
    ret = CoachSerializer.serialize('')

    assert ret == bytearray(b'\x00\x00')


def test_serialize_valid_coach():
    coach = 'Pep Guardiola'
    expected = bytearray(b'\x00\r]\xc22R\x99\x0eo\xe1E\xae\x1d\x89\xea')

    ret = CoachSerializer.serialize(coach)

    assert ret == expected
