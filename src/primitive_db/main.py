"""Точка входа в приложение primitive_db."""

from .engine import run, welcome


def main() -> None:
    """Запускает приветствие и основной цикл."""
    print("DB project is running!")
    welcome()
    run()


if __name__ == "__main__":
    main()