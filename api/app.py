import uvicorn
from fastapi import FastAPI

from .middlewares import request_handler
from .routers import setup_routes
from .documentation import setup_documentation
from .settings import api_settings, api_docs_settings

app = FastAPI(
    docs_url="/docs" if not api_docs_settings.static_path else None,
    redoc_url="/redoc" if not api_docs_settings.static_path else None
)
app.middleware("http")(request_handler)
setup_routes(app)
setup_documentation(app)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=api_settings.host,
        port=api_settings.port
    )
