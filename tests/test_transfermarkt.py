from libelifoot.provider.transfermarkt import RosterProvider, CoachProvider


ROSTER_PROV = RosterProvider()
BASE_URL = 'https://www.transfermarkt.com.br'


def test_assemble_roster_uri_with_season_year():
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('startseite')
    season = 2022

    uri = ROSTER_PROV.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{expected_id}/saison_id/{season}' == uri


def test_assemble_roster_uri_with_no_season_year():
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('startseite')

    uri = ROSTER_PROV.assemble_uri(team_id, 0)
    assert  f'{BASE_URL}/{expected_id}' == uri


def test_assemble_coach_uri():
    coach_prov = CoachProvider()
    team_id = 'manchester-united/{}/verein/985'
    expected_id = team_id.format('mitarbeiterhistorie')
    season = 2022

    uri = coach_prov.assemble_uri(team_id, season)
    assert f'{BASE_URL}/{expected_id}/personalie_id/1' == uri
