FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy only the requirements first to leverage Docker cache
COPY pyproject.toml .

# Install dependencies using uv
RUN uv pip install -r pyproject.toml

COPY src/users_service ./src/users_service
COPY src/common ./src/common

CMD ["uvicorn", "src.users_service.service:app", "--host", "0.0.0.0", "--port", "8001"] 