FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    python3.11-dev \
    libboost-all-dev \
    libgtk-3-dev \
    libgl1-mesa-dev \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

ENV DLIB_USE_CUDA=0


CMD ["python", "manage.py"]


