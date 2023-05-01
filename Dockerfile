FROM python:3.10

WORKDIR /app

COPY main.py main.py

ENTRYPOINT [ "python3", "-m" , "main"]