import newspaper

from src.summary_error import SummaryError


class Crawler:
    @classmethod
    def call(cls, url: str) -> tuple[str, str] | SummaryError:
        return cls()._call(url)

    def __init__(self) -> None:
        ...

    def _call(self, url: str) -> tuple[str, str] | SummaryError:
        article = newspaper.Article(url)
        try:
            article.download()
            article.parse()
        except newspaper.article.ArticleException as e:
            return SummaryError(error_type=SummaryError.ErrorType.FAILED_CRAWL, error_message=str(e))

        return article.title, article.text
