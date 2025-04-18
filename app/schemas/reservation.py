from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator, root_validator


FROM_TIME = (datetime.now() + timedelta(minutes=10)
             ).isoformat(timespec='minutes')
TO_TIME = (datetime.now() + timedelta(hours=1)
           ).isoformat(timespec='minutes')


class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        extra = Extra.forbid


class ReservationUpdate(ReservationBase):

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value: datetime):
        if value < datetime.now():
            raise ValueError('Past time booking!')
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values: dict):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError('Start time should be earlier than end time!')
        return values


class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int
    user_id: Optional[int]

    class Config:
        orm_mode = True
