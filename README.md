uv init fastdca_p1

cd fastdca_p1

uv venv

.venv\Scripts\activate

uv add "fastapi[standard]"

uv run python main.py

uv pip install pydantic
