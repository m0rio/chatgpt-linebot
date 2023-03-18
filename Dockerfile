FROM python:3

WORKDIR /workspace
COPY requirements.txt /workspace
RUN pip install -r requirements.txt
COPY . /workspace

VOLUME /workspace  # ホストとの共有対象とするディレクトリを指定