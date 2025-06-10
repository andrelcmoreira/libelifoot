from libelifoot.provider.espn import EspnProvider
from libelifoot.provider.transfermarkt import TransfermarktProvider


def create(
    prov_name: str
) -> EspnProvider | TransfermarktProvider | None:
    if prov_name == 'espn':
        return EspnProvider()
    if prov_name == 'transfermarkt':
        return TransfermarktProvider()

    return None
