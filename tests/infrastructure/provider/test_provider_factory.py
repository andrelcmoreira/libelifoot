from pytest import raises
from unittest.mock import MagicMock

from libelifoot.domain.error.unknown_provider import UnknownProvider
from libelifoot.infrastructure.provider import factory
from libelifoot.infrastructure.provider import espn, transfermarkt


def test_get_roster_provider_with_espn():
    provider = factory.get_roster_provider('espn', MagicMock())

    assert isinstance(provider, espn.RosterProvider)


def test_get_roster_provider_with_transfermarkt():
    provider = factory.get_roster_provider('transfermarkt', MagicMock())

    assert isinstance(provider, transfermarkt.RosterProvider)


def test_get_roster_provider_with_invalid_entry():
    provider = 'invalid_provider'

    with raises(UnknownProvider, match=f"Unknown provider '{provider}'!"):
        factory.get_roster_provider(provider, MagicMock())


def test_get_coach_provider():
    provider = factory.get_coach_provider(MagicMock())

    assert isinstance(provider, transfermarkt.CoachProvider)
