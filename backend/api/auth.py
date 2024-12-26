import logging

from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordBearer

from backend.dao.dao import UserDAO
from backend.schemas import UserSchema, TokenInfo
from backend.api import utils

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/habits")

router = APIRouter(prefix="/auth/register", tags=["auth"])




@router.post("")
async def register_user(
        user: UserSchema = Body(...),
):
    """Функция которая выпускает токен для пользователя который ввел правильный логин и пароль"""
    logger.info("Регистрируем нового пользователя")
    await UserDAO.add(
        telegram_id=user.telegram_id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
    )
    logger.info("Выдаём токен")
    jwt_payload = {
        "sub": user.first_name,
        "telegram_id": user.telegram_id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name
    }
    token = utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )


