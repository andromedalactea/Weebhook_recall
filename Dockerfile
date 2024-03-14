FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Install necessary software
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ARG data_clickgreen
ENV data_clickgreen=$data_clickgreen

COPY . .
CMD ["python", "app.py"]