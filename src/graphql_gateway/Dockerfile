FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy only the requirements first to leverage Docker cache
COPY pyproject.toml .

# Install dependencies using uv
RUN uv pip install -r pyproject.toml

COPY src/graphql_gateway ./src/graphql_gateway
COPY src/common ./src/common

CMD ["uvicorn", "src.graphql_gateway.main:app", "--host", "0.0.0.0", "--port", "8000"] 