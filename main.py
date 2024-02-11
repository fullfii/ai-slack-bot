from src.crawler import Crawler
from src.slack_sender import SlackSender
from src.summarizer import Summarizer
from src.summary_error import SummaryError
from src.url_extractor import UrlExtractor


if __name__ == "__main__":
    # input_message = "https://zenn.dev/open8/articles/python-special-method"
    input_message = "https://blog.expo.dev/expo-sdk-50-beta-is-now-available-8e6c74e4e13d"
    # input_message = "https://diamond.jp/articles/-/332258"
    # input_message = "https://twitter.com/home"

    # url_extract_result = UrlExtractor.call(input_message)
    # if type(url_extract_result) is SummaryError:
    #     SlackSender.call(url_extract_result)  # TODO
    #     exit(1)
    #
    # url, additional_message = url_extract_result
    # crawl_result = Crawler.call(url)
    # if type(crawl_result) is SummaryError:
    #     SlackSender.call(crawl_result)  # TODO
    #     exit(1)
    #
    # title, text = crawl_result
    # summary_result = Summarizer.call(title, text, additional_message)
    # if type(summary_result) is SummaryError:
    #     SlackSender.call(summary_result)
    #     exit(1)

    # SlackSender.call(summary_result)
    SlackSender.call("Hello, World!")
