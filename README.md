# <NAME>

## Setup

```bash
uv sync
```

## Development

```bash
uv run ty check
uv run ruff check
uv run ruff check --fix
uv run ruff format
uv run black .
uv run pyright
uv run <NAME>.py
```

## Testing

```bash
uv run pytest
uv run pytest --cov=.
```

## Rename the Project

Replace the `<NAME>` placeholder throughout the project:

```bash
grep -rl '<NAME>' . | xargs sed -i 's/<NAME>/<your-project-name>/g'
```

## Pre-commit

```bash
uv add --dev pre-commit
uv run pre-commit install
```

## Take up Container

	docker-compose up --build

## API Docs

Open after starting the server:

```text
http://127.0.0.1:9600/api/docs
```
