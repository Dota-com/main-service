from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AdminPermissionRequest(_message.Message):
    __slots__ = ("Email", "IsAdmin")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ISADMIN_FIELD_NUMBER: _ClassVar[int]
    Email: str
    IsAdmin: bool
    def __init__(self, Email: _Optional[str] = ..., IsAdmin: bool = ...) -> None: ...

class AdminPermissionResponse(_message.Message):
    __slots__ = ("Success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    def __init__(self, Success: bool = ...) -> None: ...

class AdminSettiongsPanelRequest(_message.Message):
    __slots__ = ("Success", "Email")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Email: str
    def __init__(self, Success: bool = ..., Email: _Optional[str] = ...) -> None: ...

class AdminSettingsPanelResponse(_message.Message):
    __slots__ = ("Service",)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    Service: int
    def __init__(self, Service: _Optional[int] = ...) -> None: ...

class AdminListInformationRequest(_message.Message):
    __slots__ = ("Success", "Email")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Email: str
    def __init__(self, Success: bool = ..., Email: _Optional[str] = ...) -> None: ...

class AdminListInformationsResponse(_message.Message):
    __slots__ = ("Service", "ServiceName")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    Service: int
    ServiceName: str
    def __init__(self, Service: _Optional[int] = ..., ServiceName: _Optional[str] = ...) -> None: ...
