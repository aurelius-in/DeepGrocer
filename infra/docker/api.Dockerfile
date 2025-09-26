FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml requirements.txt requirements-dev.txt ./
RUN pip install -U pip && pip install -r requirements.txt
COPY . .
EXPOSE 8000
