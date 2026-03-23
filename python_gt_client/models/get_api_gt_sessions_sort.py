from enum import Enum


class GetApiGtSessionsSort(str, Enum):
    CREATED_ASC = "created_asc"
    CREATED_DESC = "created_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    TITLE_ASC = "title_asc"
    TITLE_DESC = "title_desc"
    UPDATED_ASC = "updated_asc"
    UPDATED_DESC = "updated_desc"

    def __str__(self) -> str:
        return str(self.value)
