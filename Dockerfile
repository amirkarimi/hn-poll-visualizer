FROM python:3.10-slim

COPY Pipfile* /app/
WORKDIR /app
RUN pip install pipenv && \
  pipenv install --system --deploy --ignore-pipfile

COPY main.py .
ENTRYPOINT ["python", "main.py"]
