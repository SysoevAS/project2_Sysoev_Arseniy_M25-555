#!/usr/bin/env python3
"""Точка входа в приложение primitive_db."""

from .engine import run, welcome


def main() -> None:
    """Запускает приветствие и основной цикл."""
    welcome()
    run()


if __name__ == "__main__":
    main()
