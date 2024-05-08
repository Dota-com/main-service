from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResetPasswordRequests(_message.Message):
    __slots__ = ("IdUser", "Password", "Password2")
    IDUSER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD2_FIELD_NUMBER: _ClassVar[int]
    IdUser: int
    Password: str
    Password2: str
    def __init__(self, IdUser: _Optional[int] = ..., Password: _Optional[str] = ..., Password2: _Optional[str] = ...) -> None: ...

class ResetEmailRequests(_message.Message):
    __slots__ = ("IdUser", "Email")
    IDUSER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IdUser: int
    Email: str
    def __init__(self, IdUser: _Optional[int] = ..., Email: _Optional[str] = ...) -> None: ...

class ResetSteamIdRequests(_message.Message):
    __slots__ = ("IdUser", "SteamId")
    IDUSER_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    IdUser: int
    SteamId: int
    def __init__(self, IdUser: _Optional[int] = ..., SteamId: _Optional[int] = ...) -> None: ...

class ResetResponse(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...
