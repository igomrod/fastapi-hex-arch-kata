from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.post(
    "/api/todos",
    description="POST todo."
)
def post_todo():
    return PlainTextResponse(status_code=201, content="CREATED")
