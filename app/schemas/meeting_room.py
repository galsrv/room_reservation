from typing import Optional

from pydantic import BaseModel, Field, validator


# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным.
    name: str = Field(..., min_length=1, max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True


class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_cant_be_none(cls, value: str):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value
