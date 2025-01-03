import logging

from fastapi import APIRouter, Body, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import InvalidTokenError

from backend.dao.dao import UserDAO
from backend.schemas import UserSchema, TokenInfo
from backend.api import utils

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

http_bearer = HTTPBearer()

router = APIRouter(prefix="/auth", tags=["auth"])


async def get_current_token_payload(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> UserSchema:
    token = credentials.credentials
    try:
        payload = utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}"
        )
    return payload


async def get_current_auth_user(
        payload: dict = Depends(get_current_token_payload),
) -> UserSchema:
    username: str | None = payload.get("sub")
    user = await UserDAO.find_one_or_none(first_name=username)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='token invalid (user not found)'
    )


@router.post("/register")
async def register_user(
        user: UserSchema = Body(...),
):
    """Функция, которая регистрирует пользователя"""
    logger.info("Регистрируем нового пользователя")
    user_ = await UserDAO.find_one_or_none(telegram_id=user.telegram_id)
    if user_:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user already exist"
        )

    await UserDAO.add(
        telegram_id=user.telegram_id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
    )
    return {
        "result": True,
        "message": "Вы успешно зарегистрированы"
    }


@router.post("/login")
async def auth_user(
        user: UserSchema = Body(...),
):
    """Выпускаем токен для пользователя"""
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
