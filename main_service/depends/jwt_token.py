from fastapi import HTTPException

from main_service.service.jwt_decode import jwt_decode


def validateToken(text: str):
    if len(text) > 0:
        token = jwt_decode.jwt_decode(text)
        return token
        #TODO
        # if len(token) > 0:
        #     return token
        # else:
        #     return HTTPException(
        #         status_code=400,
        #         detail="Не корректные данные"
        #     )
    else:
        return HTTPException(
            status_code=400,
            detail="Пустые данные"
        )
