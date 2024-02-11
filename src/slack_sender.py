import os

from slack_sdk import WebClient


class SlackSender:
    @classmethod
    def call(cls, summary: str) -> None:
        return cls()._call(summary)

    def __init__(self) -> None:
        self.client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

    def _call(self, summary: str) -> None:
        self.client.chat_postMessage(channel='C025F0X2K3K', text=summary)
