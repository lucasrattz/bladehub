# syntax=docker/dockerfile:1
FROM python:3.11-alpine

WORKDIR /bladehub

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 2774

COPY . .

CMD ["python", "src/bladehub.py"]