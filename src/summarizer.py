import google.generativeai as genai

from src.summary_error import SummaryError


class Summarizer:
    SUMMARY_PROMPT_TEMPLATE_PATH = "prompts/summary_prompt.md"

    @classmethod
    def call(cls, title: str, text: str, additional_message: str) -> str | SummaryError:
        return cls()._call(title, text, additional_message)

    def __init__(self) -> None:
        generation_config: genai.GenerationConfig = {"temperature": 0.1}
        self.gemini_pro = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

    def _call(self, title: str, text: str, additional_message: str) -> str | SummaryError:
        prompt_template = self._read_prompt_template()
        prompt = prompt_template.format(title=title, text=text, additional_message=additional_message)  # TODO
        response = self.gemini_pro.generate_content(prompt)

        return response.text

    def _read_prompt_template(self) -> str:
        with open(self.SUMMARY_PROMPT_TEMPLATE_PATH, 'r') as file:
            prompt_template = file.read()
        return prompt_template
