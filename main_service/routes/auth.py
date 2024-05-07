from typing import Annotated

from fastapi import APIRouter, Depends

from main_service.depends import jwt_token

auth = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth.post("/register")
def register(text: Annotated[str, Depends(jwt_token.validateToken)]):
    return text

