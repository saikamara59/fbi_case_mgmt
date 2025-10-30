FROM python:3.11

RUN apt-get update --fix-missing && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    libboost-all-dev \
    libgtk-3-dev \
    libgl1-mesa-dev \
    libopenblas-dev \
    liblapack-dev \
    pkg-config \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache/pip

COPY . /app

EXPOSE 5000

ENV DLIB_USE_CUDA=0

CMD ["python", "manage.py"]

