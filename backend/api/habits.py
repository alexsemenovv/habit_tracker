import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException

from backend.schemas import SHabitIn
from backend.dao.dao import HabitDAO
from backend.models import Habit

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

router = APIRouter(prefix='/api/habits', tags=["API"])


@router.post("")
async def add_habit(habit: Annotated[SHabitIn, Depends]):
    """Добавление новой привычки"""
    logger.info('Добавляем новую привычку')

    # TODO добавить проверку пользователя по ключу

    # добавляем привычку
    new_habit: Habit = await HabitDAO.add(**habit.model_dump())
    return {
        "result": True,
        "habit_id": new_habit.id
    }


@router.delete("/{id}")
async def del_habit_by_id(id: int = Path(...)):
    """Удаление привычки"""
    logger.info('Удаление привычки по id')

    # TODO добавить проверку пользователя по ключу + получить от него id для последующего запроса

    # Проверка на существование привычки
    habit: Habit = await HabitDAO.find_one_or_none_by_id(id)
    if habit:
        result: bool = await HabitDAO.delete(habit)
        return {"result": result}
    raise HTTPException(status_code=403, detail="habit_id is not found")


@router.put("/{id}")
async def update_habit_by_id(update_habit: Annotated[SHabitIn, Depends], id: int = Path(...)):
    """Редактирование привычки"""
    logger.info('Редактирование привычки по id')

    # TODO добавить проверку пользователя по ключу + получить от него id для последующего запроса

    # Проверка на существование привычки
    habit: Habit = await HabitDAO.find_one_or_none_by_id(id)
    if habit:
        result: bool = await HabitDAO.put(habit, update_habit)
        return {"result": result}
    raise HTTPException(status_code=403, detail="habit_id is not found")
