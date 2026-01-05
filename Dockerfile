# Init Docker

FROM python3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 2210

CMD [ "python3", "app/main.py" ]