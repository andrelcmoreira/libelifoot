from libelifoot.parser.equipa import EquipaParser


def test_has_equipa_header_with_valid_equipa():
    file = 'tests/data/VALID_EQUIPA.EFT'

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        assert ep.has_equipa_header(data) is True


def test_has_equipa_header_with_invalid_equipa():
    file = 'tests/data/INVALID_EQUIPA.EFT'

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        assert ep.has_equipa_header(data) is False


def test_parse_ext_name():
    file = 'tests/data/VALID_EQUIPA.EFT'
    name = 'CR FLAMENGO'

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        assert ep.parse_ext_name(data) == name


def test_parse_short_name():
    file = 'tests/data/VALID_EQUIPA.EFT'
    ext_name = 'CR FLAMENGO'
    short_name = 'FLAMENGO'

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        assert ep.parse_short_name(data, len(ext_name)) == short_name


def test_parse_colors():
    file = 'tests/data/VALID_EQUIPA.EFT'
    ext_name = 'CR FLAMENGO'
    short_name = 'FLAMENGO'
    bg_str = 'FF0000' # red
    txt_str = '000000' # black

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        colors = ep.parse_colors(data, len(ext_name), len(short_name))

        assert str(colors) == f'#{txt_str}, #{bg_str}'
        assert colors.text == bytes.fromhex(txt_str) # FIXME
        assert colors.background == bytes.fromhex(bg_str) # FIXME


def test_parse_level():
    file = 'tests/data/VALID_EQUIPA.EFT'
    ext_name = 'CR FLAMENGO'
    short_name = 'FLAMENGO'
    level = 14

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        assert ep.parse_level(data, len(ext_name), len(short_name)) == level


def test_parse_country():
    file = 'tests/data/VALID_EQUIPA.EFT'
    ext_name = 'CR FLAMENGO'
    short_name = 'FLAMENGO'
    country = 'BRA'

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        assert ep.parse_country(data, len(ext_name), len(short_name)) == country
