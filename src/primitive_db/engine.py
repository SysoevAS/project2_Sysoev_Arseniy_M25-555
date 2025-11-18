"""Игровой цикл и базовый парсинг команд для примитивной БД."""

import shlex

import prompt


def print_help() -> None:
    """Печатает справку по доступным командам (базовая версия)."""
    print("\n***")
    print("<command> exit - выйти из программы")
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


def run() -> None:
    """Основной цикл обработки команд (пока только help/exit)."""
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

        command = tokens[0].lower()

        if command == "exit":
            print("Выход из программы.")
            break
        if command == "help":
            print_help()
            continue

        print(f"Функции {command} нет. Попробуйте снова.")
