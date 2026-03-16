from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель данных пользователя.

    Содержит информацию о пользователе системы.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(..., description="Уникальный идентификатор пользователя")
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    last_name: str = Field(..., description="Фамилия пользователя")
    first_name: str = Field(..., description="Имя пользователя")
    middle_name: str | None = Field(None, description="Отчество пользователя")
    phone_number: str | None = Field(None, description="Номер телефона пользователя")


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя.

    Используется для отправки данных при создании нового пользователя.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = Field(..., description="Электронная почта пользователя")
    last_name: str = Field(..., description="Фамилия пользователя")
    first_name: str = Field(..., description="Имя пользователя")
    middle_name: str | None = Field(None, description="Отчество пользователя")
    phone_number: str | None = Field(None, description="Номер телефона пользователя")


class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя.

    Возвращает информацию о только что созданном пользователе.
    """

    user: UserSchema = Field(..., description="Данные созданного пользователя")
