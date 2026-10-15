# MLOps HW

Шаблон Python-проекта для домашних заданий по MLOps.

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
