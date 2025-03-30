FROM python:3.10.16-slim-bullseye

WORKDIR /app

COPY requirement.txt .

RUN pip3 install --no-cache-dir -r requirement.txt 

COPY . .

EXPOSE 5000

CMD ["python3" "app.py"]