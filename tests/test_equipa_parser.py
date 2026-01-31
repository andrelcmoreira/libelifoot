from unittest import mock
from pytest import raises

from fixtures import mock_equipa, mock_players, mock_equipa_bytes

from libelifoot.parser.equipa import EquipaParser
from libelifoot.error.header_not_found import EquipaHeaderNotFound


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
    bg_str = '000000' # red
    txt_str = 'FF0000' # black

    with open(file, 'rb') as f:
        data = f.read()

        ep = EquipaParser(file)
        colors = ep.parse_colors(data, len(ext_name), len(short_name))

        assert str(colors) == f'#{bg_str}, #{txt_str}'
        assert colors.text == bytes.fromhex(txt_str)
        assert colors.background == bytes.fromhex(bg_str)


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


def test_parse_players(mock_players, mock_equipa_bytes):
    file = 'FORTALEZA.EFT'
    ext_name = 'FORTALEZA ESPORTE CLUBE'
    short_name = 'FORTALEZA'

    with mock.patch(
        'libelifoot.parser.player.PlayersParser.parse',
        return_value=mock_players
    ) as mock_parse:
        ep = EquipaParser(file)

        players = ep.parse_players(mock_equipa_bytes, len(ext_name),
                                   len(short_name))

        mock_parse.assert_called_once()
        assert players == mock_players


def test_parse_coach(mock_equipa_bytes):
    file = 'FORTALEZA.EFT'
    ext_name = 'FORTALEZA ESPORTE CLUBE'
    short_name = 'FORTALEZA'
    coach = 'Juan Pablo Vojvoda'

    with (
        mock.patch(
            'libelifoot.parser.equipa.OffsetCalculator.get_coach',
            return_value=len(mock_equipa_bytes) - 10
        ) as mock_get_coach,
        mock.patch(
            'libelifoot.util.crypto.decrypt',
            return_value=coach
        ) as mock_decrypt,
    ):
        ep = EquipaParser(file)

        ret = ep.parse_coach(mock_equipa_bytes, len(ext_name), len(short_name))

        assert ret == coach

        mock_get_coach.assert_called_once_with(
            mock_equipa_bytes,
            len(ext_name),
            len(short_name)
        )
        mock_decrypt.assert_called_once()


def test_parse_coach_with_no_info(mock_equipa_bytes):
    file = 'FORTALEZA.EFT'
    ext_name = 'FORTALEZA ESPORTE CLUBE'
    short_name = 'FORTALEZA'
    coach = 'Juan Pablo Vojvoda'

    with (
        mock.patch(
            'libelifoot.parser.equipa.OffsetCalculator.get_coach',
            return_value=len(mock_equipa_bytes) + 10
        ) as mock_get_coach,
        mock.patch(
            'libelifoot.util.crypto.decrypt',
            return_value=coach
        ) as mock_decrypt,
    ):
        ep = EquipaParser(file)

        ret = ep.parse_coach(mock_equipa_bytes, len(ext_name), len(short_name))

        assert ret == ''

        mock_get_coach.assert_called_once_with(
            mock_equipa_bytes,
            len(ext_name),
            len(short_name)
        )
        mock_decrypt.assert_not_called()


def test_parse_equipa(mock_equipa, mock_equipa_bytes):
    file = 'FORTALEZA.EFT'

    with mock.patch(
        'builtins.open',
        mock.mock_open(read_data=bytes(mock_equipa_bytes))
    ) as mock_file:
        ep = EquipaParser(file)

        equipa = ep.parse()

        assert equipa == mock_equipa
        mock_file.assert_called_once_with(file, 'rb')
        mock_file.return_value.read.assert_called_once()


def test_parse_invalid_equipa():
    file = 'FORTALEZA.EFT'

    with mock.patch(
        'builtins.open',
        mock.mock_open(read_data=bytes())
    ):
        with raises(EquipaHeaderNotFound):
            ep = EquipaParser(file)

            ep.parse()
