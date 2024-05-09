from main_service.routes import auth

from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException

from main_service.service.jwt_decode.jwt_decode import jwt_decode

app = FastAPI()

app.include_router(auth.auth)


@app.get("/test")
async def testmain(token=Depends(jwt_decode)):
    try:
        return token
    except HTTPException as e:
        raise HTTPException(
            status_code=400,
            detail=e
        )






