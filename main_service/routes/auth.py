from typing import Annotated, Any

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from main_service.grpc.auth_client import Client
from main_service.protos.gen.proto import Auth_pb2
from google.protobuf.json_format import MessageToDict
from grpc._channel import _InactiveRpcError

from main_service.shemas.auth.auth_shemas import AuthRegisterModel, AuthLoginModel

auth = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth.post("/register")
async def AuthRegisterFast(user: AuthRegisterModel, client: Any = Depends(Client)) -> JSONResponse:
    try:
        client_register = client.AuthRegistration(
            Auth_pb2.AuthRegistrationRequest(
                Email=user.email,
                Login=user.login,
                Password=user.password,
                Password2=user.password,
                SteamId=user.steam_id
            )
        )

        return JSONResponse(MessageToDict(client_register))
    except _InactiveRpcError as e:
        raise HTTPException(
            status_code=400,
            detail=e.details()
        )


@auth.post("/login")
async def AuthLoginFast(user:  AuthLoginModel, client: Any = Depends(Client)) -> JSONResponse:
    try:
        client_login = client.AuthLogin(
            Auth_pb2.AuthLoginRequest(
                Login=user.login,
                Password=user.password
            )
        )

        return JSONResponse(MessageToDict(client_login))
    except _InactiveRpcError as e:
        raise HTTPException(
            status_code=400,
            detail=e.details()
        )
