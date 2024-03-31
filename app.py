from litestar import Litestar, get
from main import Gemini, ReadingResult
from prompt import create_prompt
from result import parse_json
import json
from litestar.config.cors import CORSConfig
from litestar.config.response_cache import CACHE_FOREVER

cors_config = CORSConfig(allow_origins=["*"])

model = Gemini(streaming=False)


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/generate", cached=CACHE_FOREVER)
async def get_book(card1: str, card2: str, card3: str, question: str) -> ReadingResult:
    # with open("res.txt", "r") as f:
    #     return f.read()
    generated_response = model.invoke(
        {
            "input": create_prompt([card1, card2, card3, question])
        }
    )

    try:
        if not hasattr(generated_response.candidates[0].content.parts[0], 'text'):
            raise ValueError

        res = generated_response.candidates[0].content.parts[0].text
        parsed = parse_json(res)
        # print(json.dumps(parsed, indent=2))
        with open("res.txt", "w") as f:
            f.write(json.dumps(parsed))
        return parsed
    except ValueError as e:
        print("An error occured: ", e)


app = Litestar([index, get_book], debug=True, cors_config=cors_config)