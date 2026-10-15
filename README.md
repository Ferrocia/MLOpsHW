# MLOps Starter

Небольшой шаблон Python-проекта для домашних заданий по MLOps. Зависимостями
управляет [uv](https://docs.astral.sh/uv/), стиль кода проверяет
[Ruff](https://docs.astral.sh/ruff/), типы — [ty](https://docs.astral.sh/ty/).

## Структура

```text
.
├── pyproject.toml
├── uv.lock
├── .python-version
├── src/
│   └── mlops_starter/
│       └── __init__.py
└── tests/
    └── test_main.py
```

## Начало работы

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run ty check
```

`uv.lock` фиксирует разрешённые версии зависимостей. После изменения списка
зависимостей обновите его командой `uv lock` и добавьте файл в коммит.
