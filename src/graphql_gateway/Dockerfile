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

COPY src/graphql_gateway ./src/graphql_gateway
COPY src/common ./src/common

CMD ["/app/.venv/bin/uvicorn", "src.graphql_gateway.main:app", "--host", "0.0.0.0", "--port", "8000"] 