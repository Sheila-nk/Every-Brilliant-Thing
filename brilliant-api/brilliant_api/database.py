from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .config import settings


TORTOISE_ORM = {
    "connections": {
        "default": settings.DATABASE_URL
    },
    "apps": {
        "models": {
            "models": ["brilliant_api.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        modules={"models": ["brilliant_api.models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
