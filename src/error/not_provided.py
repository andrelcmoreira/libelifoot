
class EquipaNotProvided(Exception):

    def __init__(self, input_file: str):
        super().__init__(f"equipa '{input_file}' not available by the specified provider!")
