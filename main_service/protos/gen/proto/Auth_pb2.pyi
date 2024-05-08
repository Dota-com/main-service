from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthRegistrationRequest(_message.Message):
    __slots__ = ("Login", "Password", "Password2", "SteamId", "Email")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD2_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    Login: str
    Password: str
    Password2: str
    SteamId: int
    Email: str
    def __init__(self, Login: _Optional[str] = ..., Password: _Optional[str] = ..., Password2: _Optional[str] = ..., SteamId: _Optional[int] = ..., Email: _Optional[str] = ...) -> None: ...

class AuthLoginRequest(_message.Message):
    __slots__ = ("Login", "Password")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    Login: str
    Password: str
    def __init__(self, Login: _Optional[str] = ..., Password: _Optional[str] = ...) -> None: ...

class AuthRegistrationResponse(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...

class AuthLoginResponse(_message.Message):
    __slots__ = ("Token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    Token: str
    def __init__(self, Token: _Optional[str] = ...) -> None: ...

class AuthRolesResponse(_message.Message):
    __slots__ = ("RolesFlag", "RoleName")
    ROLESFLAG_FIELD_NUMBER: _ClassVar[int]
    ROLENAME_FIELD_NUMBER: _ClassVar[int]
    RolesFlag: int
    RoleName: str
    def __init__(self, RolesFlag: _Optional[int] = ..., RoleName: _Optional[str] = ...) -> None: ...

class AuthRolesRequest(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...

class AccessPermissionResponse(_message.Message):
    __slots__ = ("AccessPermission",)
    ACCESSPERMISSION_FIELD_NUMBER: _ClassVar[int]
    AccessPermission: str
    def __init__(self, AccessPermission: _Optional[str] = ...) -> None: ...
