import logging

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select

from backend.database import async_session

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        """
        Асинхронно находит и возвращает один экземпляр модели по указанным критериям или None.

        Аргументы:
            data_id: Критерии фильтрации в виде идентификатора записи.

        Возвращает:
            Экземпляр модели или None, если ничего не найдено.
        """
        async with async_session() as session:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """
        Асинхронно находит и возвращает один экземпляр модели по указанным критериям или None.

        Аргументы:
            **filter_by: Критерии фильтрации в виде именованных параметров.

        Возвращает:
            Экземпляр модели или None, если ничего не найдено.
        """
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        """
        Асинхронно находит и возвращает все экземпляры модели, удовлетворяющие указанным критериям.

        Аргументы:
            **filter_by: Критерии фильтрации в виде именованных параметров.

        Возвращает:
            Список экземпляров модели.
        """
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **values):
        """
        Асинхронно создает новый экземпляр модели с указанными значениями.

        Аргументы:
            **values: Именованные параметры для создания нового экземпляра модели.

        Возвращает:
            Созданный экземпляр модели.
        """
        async with async_session() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.flush()
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance

    @classmethod
    async def delete(cls, model):
        """
        Асинхронно удаляет один экземпляр модели которую передали

        Аргументы:
            model: Модель из таблицы.

        Возвращает:
            bool
        """
        async with async_session() as session:
            await session.delete(model)
            await session.commit()
            return True

    @classmethod
    async def put(cls, old_model, new_model):
        # TODO нужно удалить этот метод
        """
        Асинхронно обновляет один экземпляр переданной модели

        Аргументы:
            old_model: Старая модель
            new_model: Обновленная модель


        Возвращает:
            bool
        """
        async with async_session() as session:
            async with session.begin():
                # Закрепляем объект в текущей сессии
                db_model = await session.merge(old_model)
                # Обновляем поля
                db_model.habit_name = new_model.habit_name
                db_model.description = new_model.description
            return True

    @classmethod
    async def update(cls, instance, **fields) -> bool:
        """
        Асинхронно обновляет один экземпляр переданной модели

        Аргументы:
            instance: Экземпляр модели
            **fields: dict: Поля которые нужно обновить


        Возвращает:
            bool
        """
        logger.info(f'Обновляем переданные поля')
        async with async_session() as session:
            async with session.begin():
                # Закрепляем объект в текущей сессии
                db_model = await session.merge(instance)
                for field, value in fields.items():
                    setattr(db_model, field, value)
        return True