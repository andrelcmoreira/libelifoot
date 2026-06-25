# Copyright (C) 2025 André L. C. Moreira <andrelcmoreira@proton.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

class EquipaDataNotAvailable(Exception):

    def __init__(self, equipa: str):
        super().__init__(f"The specified provider has no data for equipa '{equipa}'!")


class EquipaHeaderNotFound(Exception):

    def __init__(self, input_file: str):
        super().__init__(f"Equipa header not found on '{input_file}'!")


class EquipaNotFound(Exception):

    def __init__(self, equipa_name: str):
        super().__init__(f"Equipa '{equipa_name}' not found!")


class EquipaNotProvided(Exception):

    def __init__(self, input_file: str):
        super().__init__(f"Equipa '{input_file}' not available by the specified provider!")


class UnknownProvider(Exception):

    def __init__(self, provider: str):
        super().__init__(f"Unknown provider '{provider}'!")
