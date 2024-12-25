from typing import Optional

from pydantic import BaseModel


class SHabitIn(BaseModel):
    habit_name: str
    description: Optional[str | None]
    user_id: int
