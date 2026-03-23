from enum import Enum


class GetApiGtGamesSort(str, Enum):
    CREATED_ASC = "created_asc"
    CREATED_DESC = "created_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)
