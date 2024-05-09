import time
import jwt

from grpc._channel import _InactiveRpcError

from fastapi.exceptions import HTTPException
from main_service.protos.gen.proto import Auth_pb2
from main_service.grpc.auth_client import Client
from google.protobuf.json_format import MessageToDict

# TODO delete it
key = 'add'


async def jwt_decode(token: str):
    try:
        token_data = jwt.decode(jwt=token, key=key, algorithms="HS256")
        result = time.time() >= (token_data["ext"] * 1000)

        if not result:
            try:
                client = await Client()
                access_token = client.AuthAccessPermission(
                    Auth_pb2.AuthLoginResponse(
                        Token=token
                    )
                )
                new_token = MessageToDict(access_token)
                return new_token["AccessPermission"]
            except _InactiveRpcError as e:
                raise HTTPException(
                    status_code=400,
                    detail=e.details()
                )
        else:
            return token
    except jwt.exceptions.DecodeError:
        return ""
