from fastapi import APIRouter

router = APIRouter(prefix="/hello-world", tags=["hello world"])


@router.get("")
def hello_world():
    return {"msg": "hello world"}
