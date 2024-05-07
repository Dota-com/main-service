import time
from datetime import datetime

import jwt

# TODO delete it
key = 'add'


def jwt_decode(token: str):
    try:
        token = jwt.decode(jwt=token, key=key, algorithms="HS256")
        result = token["ext"] - time.time()
        if result > 3600:
            # TODO Вызвать grpc запрос на обновление токена
            pass
        else:
            return token
    except jwt.exceptions.DecodeError:
        return ""
