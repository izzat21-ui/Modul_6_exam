FROM python:3.10
WORKDIR /bot
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "bot/main.py"]
