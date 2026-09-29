from libelifoot.domain.repository.equipa import IEquipaRepository
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository
from libelifoot.infrastructure.repository.file_equipa import \
    FileEquipaRepository
from libelifoot.infrastructure.repository.json_team_mapping import \
    JsonTeamMappingRepository


def get_equipa_repository() -> IEquipaRepository:
    return FileEquipaRepository()


def get_team_mapping_repository() -> ITeamMappingRepository:
    return JsonTeamMappingRepository()
