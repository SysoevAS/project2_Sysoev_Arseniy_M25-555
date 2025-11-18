"""Вспомогательные функции для работы с файлами."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List

from .constants import DATA_DIR, META_FILE


def _ensure_data_dir() -> None:
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)


def load_metadata(filepath: str = META_FILE) -> Dict[str, Any]:
    """Загружает метаданные из JSON-файла."""
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


def load_table_data(table_name: str) -> List[Dict[str, Any]]:
    """Загружает данные таблицы из JSON-файла."""
    _ensure_data_dir()
    path = os.path.join(DATA_DIR, f"{table_name}.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_table_data(table_name: str, data: List[Dict[str, Any]]) -> None:
    """Сохраняет данные таблицы в JSON-файл."""
    _ensure_data_dir()
    path = os.path.join(DATA_DIR, f"{table_name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
