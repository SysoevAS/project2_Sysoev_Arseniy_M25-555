"""Игровой цикл и парсинг команд для примитивной БД."""

import shlex
from typing import List, Tuple

import prompt

from .constants import META_FILE
from .core import create_table, drop_table
from .utils import load_metadata, save_metadata


def print_help() -> None:
    """Печатает справку по доступным командам."""
    print("\n***База данных***\n")
    print("Функции:")
    print(
        "<command> create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> .. "
        "- создать таблицу",
    )
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")


def welcome() -> None:
    """Простое приветствие через prompt."""
    name = prompt.string("May I have your name? ")
    if not name:
        name = "user"

    print(f"Привет, {name}!")
    print("***")
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация")
    print("Введите команду: help\n")


def _parse_columns(tokens: List[str]) -> List[Tuple[str, str]]:
    """Парсит список столбцов вида name:type."""
    columns: List[Tuple[str, str]] = []
    for token in tokens:
        if ":" not in token:
            raise ValueError(
                f"Некорректное значение: {token}. Попробуйте снова.",
            )
        name, col_type = token.split(":", 1)
        name = name.strip()
        col_type = col_type.strip()
        if not name or not col_type:
            raise ValueError(
                f"Некорректное значение: {token}. Попробуйте снова.",
            )
        columns.append((name, col_type))
    return columns


def _handle_create_table(tokens: List[str]) -> None:
    """Обрабатывает команду create_table."""
    if len(tokens) < 3:
        raise ValueError(
            "Некорректное значение: недостаточно аргументов. Попробуйте снова.",
        )

    table_name = tokens[1]
    raw_columns = tokens[2:]
    columns = _parse_columns(raw_columns)

    metadata = load_metadata(META_FILE)
    metadata = create_table(metadata, table_name, columns)
    save_metadata(META_FILE, metadata)

    cols_info = metadata[table_name]["columns"]
    cols_str = ", ".join(f'{c["name"]}:{c["type"]}' for c in cols_info)
    print(
        f'Таблица "{table_name}" успешно создана '
        f"со столбцами: {cols_str}",
    )


def _handle_list_tables() -> None:
    """Обрабатывает команду list_tables."""
    metadata = load_metadata(META_FILE)
    if not metadata:
        print("Таблиц пока нет.")
        return

    for name in metadata:
        print(f"- {name}")


def _handle_drop_table(tokens: List[str]) -> None:
    """Обрабатывает команду drop_table."""
    if len(tokens) != 2:
        raise ValueError(
            "Некорректное значение: нужно указать имя таблицы. "
            "Попробуйте снова.",
        )

    table_name = tokens[1]
    metadata = load_metadata(META_FILE)
    metadata = drop_table(metadata, table_name)
    save_metadata(META_FILE, metadata)
    print(f'Таблица "{table_name}" успешно удалена.')


def run() -> None:
    """Основной цикл обработки команд."""
    while True:
        try:
            user_input = input("Введите команду: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nВыход.")
            break

        if not user_input:
            continue

        tokens = shlex.split(user_input)
        if not tokens:
            continue

        command = tokens[0]

        if command == "exit":
            print("Выход из программы.")
            break

        if command == "help":
            print_help()
            continue

        if command == "create_table":
            try:
                _handle_create_table(tokens)
            except ValueError as exc:
                print(exc)
            continue

        if command == "list_tables":
            try:
                _handle_list_tables()
            except ValueError as exc:
                print(exc)
            continue

        if command == "drop_table":
            try:
                _handle_drop_table(tokens)
            except ValueError as exc:
                print(exc)
            continue

        print(f"Функции {command} нет. Попробуйте снова.")
