
class EquipaNotProvided(Exception):

    def __init__(self, input_file: str):
        super().__init__(f"Equipa '{input_file}' not available by the specified provider!")
