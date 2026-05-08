FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ . 
EXPOSE 8000

CMD ["uvicorn", "src.server:server", "--host", "0.0.0.0", "--port", "8000"]