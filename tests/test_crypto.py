from libelifoot.util.crypto import encrypt, decrypt


def test_encrypt_from_valid_string():
    expected = bytearray(b'\ru\xdaF\xb2!Mm\xe4S\xc51\x95\xb6')

    ret = encrypt('hello, world!')

    assert ret == expected


def test_encrypt_from_empty_string():
    expected = bytearray(b'\x00')

    ret = encrypt('')

    assert ret == expected


def test_decrypt_from_valid_bytearray():
    expected = 'hello, world!'
    array = b'\ru\xdaF\xb2!Mm\xe4S\xc51\x95\xb6'

    ret = decrypt(array, 1, len(array) - 1)

    assert ret == expected


def test_decrypt_from_empty_bytearray():
    expected = ''
    array = b''

    ret = decrypt(array, 0, len(array))

    assert ret == expected
