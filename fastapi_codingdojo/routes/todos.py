import fastapi.responses
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.post(
    "/api/todos",
    description="POST todo."
)
def post_todo():
    return PlainTextResponse(status_code=201, content="CREATED")

@router.get(
    "/api/todos",
    description="GET todos."
)
def get_todo():
    return fastapi.responses.JSONResponse(status_code=200, content=[])
