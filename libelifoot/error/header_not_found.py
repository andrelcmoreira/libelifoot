
class EquipaHeaderNotFound(Exception):

    def __init__(self, input_file: str):
        super().__init__(f"Equipa header not found on '{input_file}'!")
