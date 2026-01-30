from pytest import raises

from libelifoot.error.unknown_provider import UnknownProvider
from libelifoot.provider import espn
from libelifoot.provider import factory
from libelifoot.provider import transfermarkt


def test_create_roster_provider_with_espn():
    provider = factory.create_roster_provider('espn')

    assert isinstance(provider, espn.RosterProvider)


def test_create_roster_provider_with_transfermarkt():
    provider = factory.create_roster_provider('transfermarkt')

    assert isinstance(provider, transfermarkt.RosterProvider)


def test_create_roster_provider_with_invalid_entry():
    provider = 'invalid_provider'

    with raises(UnknownProvider, match=f"Unknown provider '{provider}'!"):
        factory.create_roster_provider(provider)


def test_create_coach_provider():
    provider = factory.create_coach_provider()

    assert isinstance(provider, transfermarkt.CoachProvider)
