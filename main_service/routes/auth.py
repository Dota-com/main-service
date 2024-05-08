from typing import Annotated, Any

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from main_service.grpc.auth_client import Client
from main_service.protos.gen.proto import Auth_pb2
from google.protobuf.json_format import MessageToDict
from grpc._channel import _InactiveRpcError

auth = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth.post("/register")
async def register(client: Any = Depends(Client)):
    try:
        client_register = await client.AuthRegistration(
            Auth_pb2.AuthRegistrationRequest(
                Email="",
                Login="",
                Password="",
                Password2="",
                SteamId=1
            )
        )

        return JSONResponse(MessageToDict(client_register))
    except _InactiveRpcError as e:
        raise HTTPException(
            status_code=400,
            detail=e.details()
        )


@auth.post("/login")
async def AuthLoginFast(login: str, password: str, client: Any = Depends(Client)) -> JSONResponse:
    try:
        client_login = await client.AuthLogin(
            Auth_pb2.AuthLoginRequest(
                Login=login,
                Password=password
            )
        )
        return JSONResponse(MessageToDict(client_login))

    except _InactiveRpcError as e:
        raise HTTPException(
            status_code=400,
            detail=e.details()
        )
