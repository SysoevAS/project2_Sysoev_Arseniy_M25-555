"""Вспомогательные функции для работы с метаданными."""

import json
from typing import Any, Dict

from .constants import META_FILE


def load_metadata(filepath: str = META_FILE) -> Dict[str, Any]:
    """Загружает метаданные из JSON-файла.

    Если файл отсутствует или повреждён, возвращает пустой словарь.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_metadata(filepath: str, data: Dict[str, Any]) -> None:
    """Сохраняет метаданные в JSON-файл."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
