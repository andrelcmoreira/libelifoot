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

from abc import ABC, abstractmethod


class BaseProvider(ABC):

    _USER_AGENT = 'libelifoot'
    _REQUEST_TIMEOUT = 30

    def __init__(self, provider_name: str, base_url: str, interval: int):
        self._name = provider_name
        self._base_url = base_url
        self._interval = interval

    @property
    def name(self) -> str:
        return self._name

    @property
    def interval(self) -> int:
        return self._interval

    @abstractmethod
    def assemble_uri(self, team_id: str, season: int) -> str:
        pass # pragma: no cover
