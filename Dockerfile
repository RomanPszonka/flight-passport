FROM --platform=linux/amd64 python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY uv.lock pyproject.toml ./
RUN pip install -U pip && pip install uv && uv sync --frozen --no-install-project --no-dev

RUN addgroup --gid 10000 django  && adduser --shell /bin/bash --disabled-password --gecos "" --uid 10000 --ingroup django django
RUN chown -R django:django /app
USER django:django

COPY --chown=django:django . .
RUN python manage.py collectstatic --no-input
EXPOSE 9000
