from base import BaseDAO
from backend.models import User, Habit


class UserDAO(BaseDAO):
    model = User


class ServiceDAO(BaseDAO):
    model = Habit
