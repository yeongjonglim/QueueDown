FROM python:3.8.6-slim

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt 

RUN pip install -r requirements.txt

COPY . /app
ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
