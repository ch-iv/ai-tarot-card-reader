from pathlib import Path

from litestar import Litestar, get
from litestar.template import TemplateConfig

from main import Gemini, ReadingResult
from prompt import create_prompt
from result import parse_json
import json
from litestar.config.cors import CORSConfig
from litestar.response import Template
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.static_files import create_static_files_router

cors_config = CORSConfig(allow_origins=["*"])

model = Gemini(streaming=False)


@get("/")
async def index() -> Template:
    return Template(template_name="index.html")


@get("/generate")
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


app = Litestar(
    route_handlers=[
        create_static_files_router(path="_app/immutable/assets/", directories=["front/build/_app/immutable/assets"]),
        create_static_files_router(path="_app/immutable/nodes/", directories=["front/build/_app/immutable/nodes"]),
        create_static_files_router(path="_app/immutable/chunks/", directories=["front/build/_app/immutable/chunks"]),
        create_static_files_router(path="_app/immutable/entryli/", directories=["front/build/_app/immutable/entry"]),
        index,
        get_book
    ],
    debug=True,
    cors_config=cors_config,
    template_config=TemplateConfig(
        directory=Path("front/build"),
        engine=JinjaTemplateEngine
    ),
)
