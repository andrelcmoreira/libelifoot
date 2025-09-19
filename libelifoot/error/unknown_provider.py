
class UnknownProvider(Exception):

    def __init__(self, provider: str):
        super().__init__(f"unknown provider '{provider}'!")
