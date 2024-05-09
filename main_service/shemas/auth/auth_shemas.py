import re

from pydantic import BaseModel, field_validator


class AuthRegisterModel(BaseModel):
    email: str
    password: str
    password2: str
    steam_id: int
    login: str

    @field_validator("login")
    @classmethod
    def validate_login(cls, value):
        login = len(value)
        if login < 16 or login > 4:
            return value
        raise ValueError("Не корректная длина логина")

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if not bool(re.fullmatch(r'[\w.-]+@[A-z0-9-]*\.[A-z]{2,4}', value)):
            raise ValueError("Почта не корректная")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        len_pass = len(value)
        if len_pass < 16 or len_pass > 4:
            return value
        raise ValueError("Пароль не соответствует")


class AuthLoginModel(BaseModel):
    password: str
    login: str

    @field_validator("login")
    @classmethod
    def validate_login(cls, value):
        login = len(value)
        if login > 16 or login < 4:
            raise ValueError("Короткий логин")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        len_pass = len(value)
        if len_pass < 16 or len_pass > 4:
            return value
        raise ValueError("Пароль не соответствует")
