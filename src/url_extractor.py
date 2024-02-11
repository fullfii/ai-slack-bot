import re

from src.summary_error import SummaryError


class UrlExtractor:
    @classmethod
    def call(cls, input_message: str) -> tuple[str, str] | SummaryError:
        return cls()._call(input_message)

    def __init__(self) -> None:
        ...

    def _call(self, input_message: str) -> tuple[str, str] | SummaryError:
        url_match = self._extract_url(input_message)
        if url_match is None:
            return SummaryError(error_type=SummaryError.ErrorType.NO_URL_IN_MESSAGE)
        url = url_match.group(0)
        input_message_without_url = input_message.replace(url, "")
        return url, input_message_without_url

    def _extract_url(self, input_message: str) -> re.Match[str] | None:
        return re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', input_message)
