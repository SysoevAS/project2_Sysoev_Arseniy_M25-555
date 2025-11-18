# Простая консольная база данных

Это учебный проект по Python. Здесь сделана простая консольная "база данных", которая хранит данные в JSON-файлах. Программа позволяет создавать таблицы, добавлять записи, выбирать данные, обновлять их и удалять. Проект нужен для практики работы с Python, Poetry, линтером Ruff и декораторами.

## Установка

Чтобы установить зависимости, можно использовать make:

```
make install
```

Если make недоступен:

```
poetry install
```

## Запуск программы

Запуск через make:

```
make project
```

или

```
make run
```

Запуск напрямую через poetry:

```
poetry run project
```

или:

```
poetry run database
```

После запуска программа спросит имя пользователя и откроет интерактивный ввод команд.

## Основные команды

### Управление таблицами

```
create_table <имя> <колонка:тип> ...
list_tables
drop_table <имя>
```

### Работа с данными

```
insert into <таблица> values (значения...)
select from <таблица>
select from <таблица> where <поле> = <значение>
update <таблица> set <поле> = <новое> where <поле> = <условие>
delete from <таблица> where <поле> = <значение>
info <таблица>
help
exit
```

## Пример использования

```
create_table users name:str age:int is_active:bool
insert into users values ("Sergei", 28, true)
select from users
update users set age = 29 where name = "Sergei"
delete from users where ID = 1
drop_table users
```

## Проверка качества кода

Проверка линтера Ruff:

```
make lint
```

или:

```
poetry run ruff check .
```

## Сборка и публикация пакета

Собрать пакет:

```
make build
```

Тестовая публикация:

```
make publish
```

Установка пакета в систему:

```
make package-install
```

## Демонстрация (asciinema)

https://asciinema.org/a/57SU4vsUOT517nWl7Jarr7qYv
