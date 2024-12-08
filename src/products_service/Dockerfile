FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Create and activate virtual environment
RUN uv venv .venv
ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"

# Copy only the requirements first to leverage Docker cache
COPY pyproject.toml .

# Install dependencies using uv
RUN uv pip install -r pyproject.toml

COPY src/products_service ./src/products_service
COPY src/common ./src/common

CMD ["/app/.venv/bin/uvicorn", "src.products_service.service:app", "--host", "0.0.0.0", "--port", "8002"] 