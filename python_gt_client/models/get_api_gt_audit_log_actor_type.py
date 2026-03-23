from enum import Enum


class GetApiGtAuditLogActorType(str, Enum):
    API = "api"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
