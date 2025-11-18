"""Основная логика управления таблицами (метаданные)."""

from typing import Any, Dict, List, Tuple

from .constants import VALID_TYPES


def create_table(
    metadata: Dict[str, Any],
    table_name: str,
    columns: List[Tuple[str, str]],
) -> Dict[str, Any]:
    """Создаёт новую таблицу и обновляет словарь metadata.

    columns — список пар (имя_столбца, тип).
    В начало автоматически добавляется столбец ID:int.
    """
    if table_name in metadata:
        raise ValueError(f'Ошибка: Таблица "{table_name}" уже существует.')

    full_columns: List[Tuple[str, str]] = [("ID", "int")]

    for name, col_type in columns:
        if name.lower() == "id":
            continue

        if col_type not in VALID_TYPES:
            raise ValueError(
                f"Некорректный тип столбца: {col_type}. "
                "Допустимые типы: int, str, bool.",
            )

        full_columns.append((name, col_type))

    metadata[table_name] = {
        "columns": [{"name": name, "type": col_type} for name, col_type in full_columns],
    }
    return metadata


def drop_table(metadata: Dict[str, Any], table_name: str) -> Dict[str, Any]:
    """Удаляет таблицу из metadata."""
    if table_name not in metadata:
        raise ValueError(f'Ошибка: Таблица "{table_name}" не существует.')

    del metadata[table_name]
    return metadata
