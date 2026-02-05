from libelifoot.error.unknown_provider import UnknownProvider
from libelifoot.provider import espn
from libelifoot.provider import transfermarkt


def create_coach_provider() -> transfermarkt.CoachProvider:
    return transfermarkt.CoachProvider()


def create_roster_provider(
    prov_name: str
) -> espn.RosterProvider | transfermarkt.RosterProvider:
    if prov_name == 'espn':
        return espn.RosterProvider()
    if prov_name == 'transfermarkt':
        return transfermarkt.RosterProvider()

    raise UnknownProvider(prov_name)
