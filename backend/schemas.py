from typing import Optional

from pydantic import BaseModel


class HabitSchema(BaseModel):
    habit_name: str
    description: Optional[str | None]
    user_id: int

class UserSchema(BaseModel):
    telegram_id: int
    first_name: str
    username: str
    last_name: str | None = None

class TokenInfo(BaseModel):
    access_token: str
    token_type: str
