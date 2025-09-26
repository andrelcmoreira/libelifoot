from libelifoot.provider.coach.transfermarkt import TransfermarktProvider


def create() -> TransfermarktProvider:
    return TransfermarktProvider()
