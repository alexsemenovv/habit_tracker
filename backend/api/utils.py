from datetime import timedelta, datetime

import httpx
from httpx import Response
import jwt
import bcrypt

from backend.config import settings

def encode_jwt(
        payload: dict,
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
        expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,  # срок действия токена
        expire_timedelta: timedelta | None = None,  # указываем через сколько закончится срок действия токена
):
    to_encode = payload.copy()  # копируем payload для того чтобы добавить в него ключ expire(срок действия токена)
    now = datetime.utcnow()  # получаем время по utc

    if expire_timedelta:  # если передана timedelta
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire, iat=now)  # обновляем наш словарь iat - когда был выпущен токен
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm
    )
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded


def hash_password(
        password: str,
) -> bytes:
    """Здесь мы хэшируем пароль"""
    salt = bcrypt.gensalt()  # генерируем соль
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
        password: str,
        hashed_password: bytes,
) -> bool:
    """Функция для проверки захеширвоанного пароля"""
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password
    )



async def send_data(url: str, data: dict, headers: dict = None) -> Response:
    """Функция для отправки запросов"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            headers=headers,
            json=data,
            timeout=5
        )
        return response
