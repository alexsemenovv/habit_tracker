from typing import List

from sqlalchemy import INTEGER, Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, relationship

from backend.database import Base


class User(Base):
    """ Класс `пользователь` """
    __tablename__: str = "users"

    id: Mapped[int] = Column(INTEGER, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = Column(BigInteger, nullable=False)
    first_name: Mapped[str] = Column(String, nullable=False, index=True)
    last_name: Mapped[str] = Column(String)
    username: Mapped[str] = Column(String, nullable=False, index=True)
    token: Mapped[str] = Column(String, nullable=True, index=True)

    habits: Mapped[List["Habit"]] = relationship("Habit", back_populates="user", cascade="all, delete-orphan")


class Habit(Base):
    """ Класс `привычка` """
    __tablename__: str = "habits"

    id: Mapped[int] = Column(BigInteger, primary_key=True, autoincrement=True)
    habit_name: Mapped[str] = Column(String, nullable=False, index=True)
    description: Mapped[str] = Column(String)
    user_id: Mapped[int] = Column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="habits")
