from libelifoot.error.unknown_provider import UnknownProvider
from libelifoot.provider.roster.espn import EspnProvider
from libelifoot.provider.roster.transfermarkt import TransfermarktProvider


def create(prov_name: str) -> EspnProvider | TransfermarktProvider:
    if prov_name == 'espn':
        return EspnProvider()
    if prov_name == 'transfermarkt':
        return TransfermarktProvider()

    raise UnknownProvider(prov_name)
