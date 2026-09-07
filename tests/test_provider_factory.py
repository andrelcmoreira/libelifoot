from pytest import raises
from unittest.mock import MagicMock

from libelifoot.domain.error.unknown_provider import UnknownProvider
from libelifoot.infrastructure.provider import factory
from libelifoot.infrastructure.provider.impl import espn
from libelifoot.infrastructure.provider.impl import transfermarkt


def test_create_roster_provider_with_espn():
    provider = factory.create_roster_provider('espn', MagicMock())

    assert isinstance(provider, espn.RosterProvider)


def test_create_roster_provider_with_transfermarkt():
    provider = factory.create_roster_provider('transfermarkt', MagicMock())

    assert isinstance(provider, transfermarkt.RosterProvider)


def test_create_roster_provider_with_invalid_entry():
    provider = 'invalid_provider'

    with raises(UnknownProvider, match=f"Unknown provider '{provider}'!"):
        factory.create_roster_provider(provider, MagicMock())


def test_create_coach_provider():
    provider = factory.create_coach_provider(MagicMock())

    assert isinstance(provider, transfermarkt.CoachProvider)
