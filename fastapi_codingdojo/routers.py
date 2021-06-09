from fastapi import FastAPI

from .routes import api, todos


def setup_routes(app: FastAPI):
    """Each Router specified in routes/* must be referenced in setup_routes(),
    as a new app.include_router() call."""
    app.include_router(
        api.router,
        prefix="",
        tags=["api"]
    )
    app.include_router(
        todos.router,
        prefix="",
        tags=["todos"]
    )


TAGS_METADATA = [
    {
        "name": "api",
        "description": "General system endpoints for the API."
    }
]
"""Tags are used in generated documentation for grouping endpoints.
In the metadata a description can be provided for each tag.
It is not mandatory to declare all tags in this array - only tags where the description is set."""
