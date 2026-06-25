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
from typing import Optional

from libelifoot.use_case.dto import Equipa


class IUpdateEquipaListener(ABC): # pragma: no cover

    @abstractmethod
    def on_update_equipa(
        self,
        equipa_name: str,
        equipa_data: Optional[Equipa]
    ) -> None:
        """
        Invoked when an equipa is successfully updated.

        :equipa_name: The name of the equipa.
        :equipa_data: The updated equipa data.
        """

    @abstractmethod
    def on_update_equipa_error(self, error: str) -> None:
        """
        Invoked when there is an error updating an equipa.

        :error: The error message.
        """
