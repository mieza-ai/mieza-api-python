from enum import Enum


class GetApiGtPlaysStatus(str, Enum):
    COMPLETE = "complete"
    CREATED = "created"
    FAILED = "failed"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
