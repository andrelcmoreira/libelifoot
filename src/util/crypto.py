
def encrypt(text: str) -> bytearray:
    out = bytearray()

    out.append(len(text))
    for i in range(0, len(text)):
        out.append((ord(text[i]) + out[i]) & 0xff)

    return out


def decrypt(data: bytes, offset: int, size: int) -> str:
    ret = ''

    for i in range(offset, offset + size):
        ret += chr((data[i] - data[i - 1]) & 0xff) # picking only the 8 less
                                                   # significant bits

    return ret
