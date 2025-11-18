"""Декораторы и замыкания для проекта."""

from __future__ import annotations

import functools
import time
from typing import Any, Callable, Dict

FuncType = Callable[..., Any]


def handle_db_errors(func: FuncType) -> FuncType:
    """Декоратор для обработки ошибок БД."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(
                "Ошибка: Файл данных не найден. "
                "Возможно, база данных не инициализирована.",
            )
        except ValueError as exc:
            print(exc)
        except KeyError as exc:
            name = exc.args[0]
            print(f'Ошибка: Таблица "{name}" не существует.')
        except Exception as exc:  # noqa: BLE001
            print(f"Произошла непредвиденная ошибка: {exc}")
        return None

    return wrapper  # type: ignore[return-value]


def confirm_action(action_name: str) -> Callable[[FuncType], FuncType]:
    """Декоратор для подтверждения опасных операций."""

    def decorator(func: FuncType) -> FuncType:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            answer = input(
                f'Вы уверены, что хотите выполнить "{action_name}"? [y/n]: ',
            ).strip().lower()
            if answer != "y":
                print("Операция отменена.")
                return None
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator


def log_time(func: FuncType) -> FuncType:
    """Декоратор для измерения времени выполнения функции."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.monotonic()
        result = func(*args, **kwargs)
        elapsed = time.monotonic() - start
        print(f"Функция {func.__name__} выполнилась за {elapsed:.3f} секунд.")
        return result

    return wrapper  # type: ignore[return-value]


def create_cacher() -> Callable[[Any, Callable[[], Any]], Any]:
    """Создаёт функцию-замыкание для кэширования результатов."""
    cache: Dict[Any, Any] = {}

    def cache_result(key: Any, value_func: Callable[[], Any]) -> Any:
        if key in cache:
            return cache[key]
        value = value_func()
        cache[key] = value
        return value

    return cache_result
