import enum
from dataclasses import dataclass


@dataclass
class SummaryError:
    class ErrorType(enum.IntEnum):
        NO_URL_IN_MESSAGE = enum.auto()
        FAILED_CRAWL = enum.auto()

    error_type: ErrorType
    error_message: str = None

    def __str__(self) -> str:
        msg = self.error_type.name
        if self.error_message:
            msg += f": {self.error_message}"
        return msg
