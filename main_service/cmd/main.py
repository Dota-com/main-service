from typing import Annotated

import fastapi.exceptions
from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()


def validate(text: str):
    if text != " ":
        return text.upper()
    else:
        return HTTPException(
            status_code=400,
            detail="Пустые данные"
        )

@app.post("/auth/register")
def register(text: Annotated[str, Depends(validate)]):
    return text




