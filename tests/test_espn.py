from libelifoot.provider.espn import RosterProvider


ROSTER_PROV = RosterProvider()
BASE_URL = 'https://www.espn.com.br/futebol/time/elenco/_/id'


def test_assemble_roster_uri_with_season_year():
    team_id = '360'
    season = 2022

    uri = ROSTER_PROV.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{team_id}/season/{season}' == uri


def test_assemble_roster_uri_with_no_season_year():
    team_id = '360'

    uri = ROSTER_PROV.assemble_uri(team_id, 0)
    assert  f'{BASE_URL}/{team_id}' == uri
