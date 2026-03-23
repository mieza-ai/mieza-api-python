from enum import Enum


class GetApiGtPlaysSourcesItem(str, Enum):
    API = "API"
    SITE = "Site"
    UPLOAD = "Upload"

    def __str__(self) -> str:
        return str(self.value)
