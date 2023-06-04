from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, Field, validator
from pydantic.types import constr


class LoginSerializer(BaseModel):
    username: str
    password: constr(strip_whitespace=True, min_length=8)


class UserSerializer(BaseModel):
    salary: float
    update_salary: datetime

    class Config:
        orm_mode = True


class TokenSerializer(BaseModel):
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

    @validator("token")
    def hexlify_token(cls, value):
        return value.hex
