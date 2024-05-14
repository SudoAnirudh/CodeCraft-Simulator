# Backend
FROM python:3.8-slim

WORKDIR /app

COPY ./backend /app/backend
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "backend/app.py"]
