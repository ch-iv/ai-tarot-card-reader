import json
from vertexai.generative_models import GenerativeModel, Part, HarmCategory, HarmBlockThreshold, GenerationConfig, Content
from deck import tarot_deck
from prompt import create_prompt
import random
from result import parse_json
from dataclasses import dataclass


@dataclass
class CardInterpretation:
    card: str
    interpretation: str


@dataclass
class ReadingResult:
    cards: list[CardInterpretation]
    summary: str
    advice: list[str]


class Gemini:
    def __init__(self, streaming: bool = False):
        self.model = GenerativeModel("gemini-1.0-pro")
        self.streaming = streaming

        self.config = GenerationConfig(
            temperature=1,
            top_p=1,
            top_k=40,
            candidate_count=1,
            max_output_tokens=2048,
        )

        # !!! UNSAFE !!! change later to a more strict harm block category
        # This has been set for testing purposes.
        self.safety_config = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
        }

    def invoke(self, prompt: dict):
        user_input = Content(
            role="user",
            parts=[
                Part.from_text(prompt["input"]),
            ]
        )

        response = self.model.generate_content(
            contents=user_input,
            generation_config=self.config,
            safety_settings=self.safety_config,
            stream=self.streaming,
            tools=[]
        )

        return response


def generate_random_cards(n: int) -> list[str]:
    return random.sample(tarot_deck, n)


if __name__ == "__main__":
    model = Gemini(streaming=False)

    generated_response = model.invoke(
        {
            "input": create_prompt([*generate_random_cards(3), "finding a good place to have dinner"])
        }
    )

    try:
        if not hasattr(generated_response.candidates[0].content.parts[0], 'text'):
            raise ValueError

        res = generated_response.candidates[0].content.parts[0].text
        parsed = parse_json(res)
        print(json.dumps(parsed, indent=2))
    except ValueError as e:
        print("An error occured: ", e)

