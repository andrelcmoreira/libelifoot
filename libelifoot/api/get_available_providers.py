from typing import Any

from libelifoot.api.base_cmd import BaseCmd
from libelifoot.provider import db


class Cmd(BaseCmd):

    def run(self) -> Any:
        return db.get_available_providers()
