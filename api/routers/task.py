from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    return {"message": "hello world!"}


@router.post("/tasks")
async def create_task():
    pass