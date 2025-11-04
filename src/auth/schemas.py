from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl
from typing import Optional
from datetime import datetime


NAME_PATTERN = r"^[А-Яа-яA-Za-z\- ]+$"  # ФИО: буквы, пробелы, дефисы
USERNAME_PATTERN = r"^@[a-zA-Z0-9_]{5,32}$"  # @username, 5-32 символа


# USER -------------------------------------
class UserSchema(BaseModel):
    email: EmailStr
    username: Optional[str] = Field(min_length=5, max_length=30)
    first_name: str = Field(min_length=1, max_length=256, pattern=NAME_PATTERN, examples=['Иван'])
    surname: str = Field(min_length=1, max_length=256, pattern=NAME_PATTERN, examples=['Иванов'])
    patronymic: Optional[str] = Field(min_length=1, max_length=256, pattern=NAME_PATTERN, description="Отчество, если есть", examples=['Иванович'])
    avatar_url: str
    status: Optional[str] = Field(max_length=256, description="Статус пользователя")
    gender: Optional[str] = Field(default="не указан", max_length=10, description="Пол пользователя")
    telegram_contact: Optional[str] = Field(max_length=256, pattern=USERNAME_PATTERN, examples=["@username"])
    github_contact: Optional[HttpUrl] = Field(max_length=256, examples=["https://github.com/user"])
    leetcode_contact: Optional[HttpUrl] = Field(max_length=256, examples=["https://leetcode.com/user"])
    stackoverflow_contact: Optional[HttpUrl] = Field(max_length=256, examples=["https://stackoverflow.com/users/123456"])
    balance: int = Field(default=0, ge=0)
    happy_birthday: Optional[datetime]


class UserCreate(UserSchema):
    password: Optional[str] = Field(min_length=8, max_length=256, description="Пароль пользователя. Необязателен при OAuth")


class UserRead(UserSchema):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    username: Optional[str] = Field(min_length=5, max_length=30)
    first_name: Optional[str] = Field(min_length=1, max_length=256, pattern=NAME_PATTERN)
    surname: Optional[str] = Field(min_length=1, max_length=256, pattern=NAME_PATTERN)
    patronymic: Optional[str] = Field(min_length=1, max_length=256, pattern=NAME_PATTERN)
    avatar_url: Optional[HttpUrl]
    status: Optional[str] = Field(max_length=256)
    gender: Optional[str] = Field(max_length=10)
    telegram_contact: Optional[str] = Field(max_length=256, pattern=USERNAME_PATTERN)
    github_contact: Optional[HttpUrl]
    leetcode_contact: Optional[HttpUrl]
    stackoverflow_contact: Optional[HttpUrl]
    balance: Optional[int] = Field(ge=0)
    happy_birthday: Optional[datetime]
    password: Optional[str] = Field(min_length=8, max_length=256)
# ------------------------------------------


# OAUTH ------------------------------------
class OAuthAccountRead(BaseModel):
    provider: str
    provider_user_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
# ------------------------------------------